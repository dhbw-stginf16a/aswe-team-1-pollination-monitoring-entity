#!/usr/bin/env python3

import logging
import requests
import json
logger = logging.getLogger(__name__)


def getPollination(body):
    r = requests.get('https://opendata.dwd.de/climate_environment/health/alerts/s31fg.json')
    data = r.json()
    data_filtered = [x for x in data['content'] if x['partregion_name'] == body['payload']['region']]
    response = {
        'type': body['payload']['day'],
        'payload': {
            'pollination': {
                'region': data_filtered[0]['region_name'],
                'partregion': data_filtered[0]['partregion_name'],
                'day': body['payload']['day']
            }
        }
    }
    if body["payload"]['pollen']['esche'] == 'true': response['payload']['pollination'].update({'esche': data_filtered[0]['Pollen']['Esche'][body['payload']['day']]})
    if body["payload"]['pollen']['beifuss'] == 'true': response['payload']['pollination'].update({'beifuss': data_filtered[0]['Pollen']['Beifuss'][body['payload']['day']]})
    if body["payload"]['pollen']['graeser'] == 'true': response['payload']['pollination'].update({'graeser': data_filtered[0]['Pollen']['Graeser'][body['payload']['day']]})
    if body["payload"]['pollen']['roggen'] == 'true': response['payload']['pollination'].update({'roggen': data_filtered[0]['Pollen']['Roggen'][body['payload']['day']]})
    if body["payload"]['pollen']['erle'] == 'true': response['payload']['pollination'].update({'erle': data_filtered[0]['Pollen']['Erle'][body['payload']['day']]})
    if body["payload"]['pollen']['ambrosia'] == 'true': response['payload']['pollination'].update({'ambrosia': data_filtered[0]['Pollen']['Ambrosia'][body['payload']['day']]})
    if body["payload"]['pollen']['hasel'] == 'true': response['payload']['pollination'].update({'hasel': data_filtered[0]['Pollen']['Hasel'][body['payload']['day']]})
    if body["payload"]['pollen']['birke'] == 'true': response['payload']['pollination'].update({'birke': data_filtered[0]['Pollen']['Birke'][body['payload']['day']]})
    return [response], 200