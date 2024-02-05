
# Daily Weather

Minute weather measurements

## Structure

`DailyWeather`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `float` | Optional | Weather condition id |
| `main` | `str` | Optional | Group of weather parameters (Rain, Snow etc.) |
| `description` | `str` | Optional | Weather condition within the group (full list of weather conditions). Get the output in your language |
| `icon` | `str` | Optional | Weather icon id. |

## Example (as JSON)

```json
{
  "id": 803.0,
  "main": "Clouds",
  "description": "broken clouds",
  "icon": "04n"
}
```

