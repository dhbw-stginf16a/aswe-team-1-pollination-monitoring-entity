#!/usr/bin/env python3

import logging
import requests
import json
logger = logging.getLogger(__name__)


def getPollination(body):
    r = requests.get("https://opendata.dwd.de/climate_environment/health/alerts/s31fg.json")
    data = r.json()
    data_filtered = [x for x in data["content"] if x["partregion_name"] == body["payload"]["region"]]
    response = {
        "type": body["payload"]["day"],
        "payload": {
            "pollination": {
                "region": data_filtered[0]["region_name"],
                "partregion": data_filtered[0]["partregion_name"],
                "day": body["payload"]["day"]
            }
        }
    }

    req_day = body["payload"]["day"]
    allergies = body["payload"]["pollen"]
    resp_poll = {}

    if allergies.setdefault("esche", "false") == "true": resp_poll.update({"esche": data_filtered[0]["Pollen"]["Esche"][req_day]})
    if allergies.setdefault("beifuss", "false") == "true": resp_poll.update({"beifuss": data_filtered[0]["Pollen"]["Beifuss"][req_day]})
    if allergies.setdefault("graeser", "false") == "true": resp_poll.update({"graeser": data_filtered[0]["Pollen"]["Graeser"][req_day]})
    if allergies.setdefault("roggen", "false") == "true": resp_poll.update({"roggen": data_filtered[0]["Pollen"]["Roggen"][req_day]})
    if allergies.setdefault("erle", "false") == "true": resp_poll.update({"erle": data_filtered[0]["Pollen"]["Erle"][req_day]})
    if allergies.setdefault("ambrosia", "false") == "true": resp_poll.update({"ambrosia": data_filtered[0]["Pollen"]["Ambrosia"][req_day]})
    if allergies.setdefault("hasel", "false") == "true": resp_poll.update({"hasel": data_filtered[0]["Pollen"]["Hasel"][req_day]})
    if allergies.setdefault("birke", "false") == "true": resp_poll.update({"birke": data_filtered[0]["Pollen"]["Birke"][req_day]})

    response["payload"]["pollination"] = resp_poll
    return [response], 200