
# Alert

National weather alerts data from major national weather warning systems

## Structure

`Alert`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sender_name` | `str` | Optional | Name of the alert source. Please read here the full list of alert sources |
| `event` | `str` | Optional | Alert event name |
| `start` | `float` | Optional | Date and time of the start of the alert, Unix, UTC |
| `end` | `float` | Optional | Date and time of the end of the alert, Unix, UTC |
| `description` | `str` | Optional | Description of the alert |
| `tags` | `List[str]` | Optional | Type of severe weather |

## Example (as JSON)

```json
{
  "sender_name": "NWS Philadelphia - Mount Holly (New Jersey, Delaware, Southeastern Pennsylvania)",
  "event": "Small Craft Advisory",
  "start": 1684952747.0,
  "end": 1684988747.0,
  "description": "...SMALL CRAFT ADVISORY REMAINS IN EFFECT FROM 5 PM THIS\nAFTERNOON TO 3 AM EST FRIDAY...\n* WHAT...North winds 15 to 20 kt with gusts up to 25 kt and seas\n3 to 5 ft expected.\n* WHERE...Coastal waters from Little Egg Inlet to Great Egg\nInlet NJ out 20 nm, Coastal waters from Great Egg Inlet to\nCape May NJ out 20 nm and Coastal waters from Manasquan Inlet\nto Little Egg Inlet NJ out 20 nm.\n* WHEN...From 5 PM this afternoon to 3 AM EST Friday.\n* IMPACTS...Conditions will be hazardous to small craft.",
  "tags": [
    "TBD"
  ]
}
```

