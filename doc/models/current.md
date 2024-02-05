
# Current

Current weather data API response

## Structure

`Current`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dt` | `float` | Optional | Current time, Unix, UTC |
| `sunrise` | `float` | Optional | Sunrise time, Unix, UTC. For polar areas in midnight sun and polar night periods this parameter is not returned in the response |
| `sunset` | `float` | Optional | Sunset time, Unix, UTC. For polar areas in midnight sun and polar night periods this parameter is not returned in the response |
| `temp` | `float` | Optional | Temperature. Units - default: kelvin, metric: Celsius, imperial: Fahrenheit. How to change units used |
| `feels_like` | `float` | Optional | Temperature. This temperature parameter accounts for the human perception of weather. Units – default: kelvin, metric: Celsius, imperial: Fahrenheit. |
| `pressure` | `float` | Optional | Atmospheric pressure on the sea level, hPa |
| `humidity` | `float` | Optional | Humidity, % |
| `dew_point` | `float` | Optional | Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form. Units – default: kelvin, metric: Celsius, imperial: Fahrenheit |
| `uvi` | `float` | Optional | Current UV index. |
| `clouds` | `float` | Optional | Cloudiness, % |
| `visibility` | `float` | Optional | Average visibility, metres. The maximum value of the visibility is 10 km |
| `wind_speed` | `float` | Optional | Wind speed. Wind speed. Units – default: metre/sec, metric: metre/sec, imperial: miles/hour. How to change units used |
| `wind_deg` | `float` | Optional | Wind direction, degrees (meteorological) |
| `wind_gust` | `float` | Optional | (where available) Wind gust. Units – default: metre/sec, metric: metre/sec, imperial: miles/hour. How to change units used |
| `rain` | [`HourlyRain`](../../doc/models/hourly-rain.md) | Optional | Minute weather measurements |
| `snow` | [`HourlySnow`](../../doc/models/hourly-snow.md) | Optional | Minute weather measurements |
| `weather` | [`List[CurrentWeather]`](../../doc/models/current-weather.md) | Optional | current weather details |

## Example (as JSON)

```json
{
  "dt": 1706746144.0,
  "sunrise": 1706741791.0,
  "sunset": 1706778792.0,
  "temp": 269.82,
  "feels_like": 262.82,
  "pressure": 1034,
  "humidity": 62,
  "dew_point": 264.27,
  "uvi": 0.26,
  "clouds": 100,
  "visibility": 10000,
  "wind_speed": 12.59,
  "wind_deg": 19,
  "wind_gust": 13.37,
  "weather": [
    {
      "id": 804,
      "main": "Clouds",
      "description": "overcast clouds",
      "icon": "04d"
    }
  ]
}
```

