#!/usr/bin/env python3

import logging
import os
import time

import requests
import connexion
from flask_cors import CORS
from requests.exceptions import ConnectionError

logger = logging.getLogger(__name__)


CENTRAL_NODE_BASE_URL = os.environ.setdefault("CENTRAL_NODE_BASE_URL", "http://localhost:8080/api/v1")
OUR_URL = os.environ.setdefault("OWN_URL", "http://localhost:8081/api/v1")

app = connexion.App(__name__, specification_dir='openapi/')
app.add_api('openapi.yml')

# Set CORS headers
CORS(app.app)

# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

logger.info('App initialized')

logger.info('Updater intialized')


# Try to register the application on app startup
#@application.before_first_request
def register():
    while True:
        logger.info("Attempt registration")
        try:
            r = requests.post("{}/monitoring".format(CENTRAL_NODE_BASE_URL), json = { "name": "pollination", "endpoint": OUR_URL, "concern": 'pollination'})
            if r.status_code == 204:
                logger.info("Registered")
                break
        except ConnectionError as conn:
            logger.warning('Attempted registration failed: %s', conn)
            logger.warning('Retrying in 5 seconds')

        time.sleep(5)