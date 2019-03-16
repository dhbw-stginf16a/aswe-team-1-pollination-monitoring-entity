#!/usr/bin/env python3

import logging

logger = logging.getLogger(__name__)

def eventToJSON(event, day):
    return {
        'region_name': event.region_name,
        'partregion_name': event.partregion_name,
        'Esche': event.Pollen.Esche.day,
        'Beifuss': event.Pollen.Beifuss.day,
        'Graeser': event.Pollen.Graeser.day,
        'Roggen': event.Pollen.Roggen.day,
        'Erle': event.Pollen.Erle.day,
        'Ambrosia': event.Pollen.Ambrosia.day,
        'Hasel': event.Pollen.Hasel.day,
        'Birke': event.Pollen.Birke.day,
        'location': event.location,
}