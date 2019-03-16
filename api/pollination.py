#!/usr/bin/env python3

import logging
import requests
import json
logger = logging.getLogger(__name__)
from api.models.utils import eventToJSON


def getPollination(body):
    r = requests.get('https://opendata.dwd.de/climate_environment/health/alerts/s31fg.json')
    data = r.json()
    data_filtered = [x for x in data['content'] if x['partregion_name'] == body['payload']['region']]
    response = {
        'type': body['payload']['day'],
        'payload': {
            'region': data_filtered[0]['region_name'],
            'partregion': data_filtered[0]['partregion_name'],
            'esche': data_filtered[0]['Pollen']['Esche'][body['payload']['day']],
            'beifuss': data_filtered[0]['Pollen']['Beifuss']['today'],
            'graeser': data_filtered[0]['Pollen']['Graeser']['today'],
            'roggen': data_filtered[0]['Pollen']['Roggen']['today'],
            'erle': data_filtered[0]['Pollen']['Erle']['today'],
            'ambrosia': data_filtered[0]['Pollen']['Ambrosia']['today'],
            'hasel': data_filtered[0]['Pollen']['Hasel']['today'],
            'birke': data_filtered[0]['Pollen']['Birke']['today'],
            'day': body['payload']['day']
        }
    }
    return [response], 200