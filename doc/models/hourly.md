
# Hourly

Minute weather measurements

## Structure

`Hourly`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dt` | `float` | Optional | Time of the forecasted data, unix, UTC |
| `temp` | `float` | Optional | Temperature. Units – default: kelvin, metric: Celsius, imperial: Fahrenheit. How to change units used |
| `feels_like` | `float` | Optional | Tempreature - This accounts for the human perception of weather. Units – default: kelvin, metric: Celsius, imperial: Fahrenheit. |
| `pressure` | `float` | Optional | Atmospheric pressure on the sea level, hPa |
| `humidity` | `float` | Optional | Humidity, % |
| `dew_point` | `float` | Optional | Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form. Units – default: kelvin, metric: Celsius, imperial: Fahrenheit. |
| `uvi` | `float` | Optional | UV index |
| `clouds` | `float` | Optional | Cloudiness % |
| `visibility` | `float` | Optional | Average visibility, metres. The maximum value of the visibility is 10 km |
| `wind_speed` | `float` | Optional | Wind speed. Units – default: metre/sec, metric: metre/sec, imperial: miles/hour.How to change units used |
| `wind_gust` | `float` | Optional | (where available) Wind gust. Units – default: metre/sec, metric: metre/sec, imperial: miles/hour. How to change units used |
| `wind_deg` | `float` | Optional | Wind direction, degrees (meteorological) |
| `pop` | `float` | Optional | Probability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100% |
| `rain` | [`HourlyRain`](../../doc/models/hourly-rain.md) | Optional | Minute weather measurements |
| `snow` | [`HourlySnow`](../../doc/models/hourly-snow.md) | Optional | Minute weather measurements |
| `weather` | [`List[HourlyWeather]`](../../doc/models/hourly-weather.md) | Optional | current weather details |

## Example (as JSON)

```json
{
  "dt": 1684926000.0,
  "temp": 292.01,
  "feels_like": 292.33,
  "pressure": 1014.0,
  "humidity": 91.0,
  "dew_point": 290.51,
  "uvi": 0,
  "clouds": 54,
  "visibility": 10000,
  "wind_speed": 2.58,
  "wind_gust": 5.88,
  "wind_deg": 86,
  "pop": 0.15
}
```

