
# Weather Info

Successful response

## Structure

`WeatherInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lat` | `float` | Optional | Latitude of the location, decimal (−90; 90) |
| `lon` | `float` | Optional | Longitude of the location, decimal (-180; 180) |
| `timezone` | `str` | Optional | Timezone name for the requested location |
| `timezone_offset` | `float` | Optional | Shift in seconds from UTC |
| `current` | [`Current`](../../doc/models/current.md) | Optional | Current weather data API response |
| `minutely` | [`Minutely`](../../doc/models/minutely.md) | Optional | Minute weather measurements |
| `hourly` | [`Hourly`](../../doc/models/hourly.md) | Optional | Minute weather measurements |
| `daily` | [`List[Daily]`](../../doc/models/daily.md) | Optional | List of National weather alert messagess |
| `alerts` | [`List[Alert]`](../../doc/models/alert.md) | Optional | List of National weather alert messagess |

## Example (as JSON)

```json
{
  "lat": 37.8349,
  "lon": 122.1297,
  "timezone": "Etc/GMT-8",
  "timezone_offset": 28800.0,
  "current": {
    "dt": 245.38,
    "sunrise": 34.46,
    "sunset": 21.86,
    "temp": 15.48,
    "feels_like": 195.38
  }
}
```

