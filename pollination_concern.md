# Concern Definition (Pollination)

**Concern-Tag :** `pollination`

This is all about pollination events.

## General Parameters

* **type** (dictionary) The day that the information is for (today, tomorrow or dayafter_tomorrow)
* **pollination** (dictionary) The pollination of the requested day in the requested area
    - ambrosia
    - beifuss
    - birke
    - erle
    - esche
    - graeser
    - hasel
    - roggen
    - day
    - partregion
    - region

## Request Types

### Pollination for a given day in a given partregion 

**Type-Tag:** `event_pollination`

#### Request

- **day** (string): Day of interest (either today, tomorrow or dayafter_tomorrow)
- **region**: (string): Region of interest. Has to match one of the "part_regions"

#### Response

- **type**: Array as listed in general parameters
- **pollination**: Array as listed in general parameters

#### Example

Request

```json
{
    'type': 'current_pollination',
    'payload': {
        "region": "Mainfranken",
        "day": "tomorrow"
    }
}
```

Response

```json
[
  {
    "pollination": {
      "ambrosia": "0",
      "beifuss": "0",
      "birke": "0",
      "day": "tomorrow",
      "erle": "2",
      "esche": "0-1",
      "graeser": "0",
      "hasel": "1",
      "partregion": "Mainfranken",
      "region": "Bayern",
      "roggen": "0"
    },
    "type": "tomorrow"
  }
]
```



