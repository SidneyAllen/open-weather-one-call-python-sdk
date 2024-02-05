
# Current Weather

current weather measurements

## Structure

`CurrentWeather`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `float` | Optional | Weather condition id |
| `main` | `str` | Optional | Group of weather parameters (Rain, Snow etc.) |
| `description` | `str` | Optional | Weather condition within the group (full list of weather conditions). Get the output in your language |
| `icon` | `str` | Optional | Weather icon id. How to get icons |

## Example (as JSON)

```json
{
  "id": 804.0,
  "main": "Clouds",
  "description": "overcast clouds",
  "icon": "04d"
}
```

