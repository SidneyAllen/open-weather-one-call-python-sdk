
# Daily

Daily forecast weather data API response

## Structure

`Daily`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dt` | `float` | Optional | Time of the forecasted data, Unix, UTC |
| `sunrise` | `float` | Optional | Sunrise time, Unix, UTC. For polar areas in midnight sun and polar night periods this parameter is not returned in the response |
| `sunset` | `float` | Optional | Sunset time, Unix, UTC. For polar areas in midnight sun and polar night periods this parameter is not returned in the response |
| `moonrise` | `float` | Optional | The time of when the moon rises for this day, Unix, UTC |
| `moonset` | `float` | Optional | The time of when the moon rises for this day, Unix, UTC |
| `moon_phase` | `float` | Optional | Moon phase. 0 and 1 are 'new moon', 0.25 is 'first quarter moon', 0.5 is 'full moon' and 0.75 is 'last quarter moon'. The periods in between are called 'waxing crescent', 'waxing gibbous', 'waning gibbous', and 'waning crescent', respectively. Moon phase calculation algorithm: if the moon phase values between the start of the day and the end of the day have a round value (0, 0.25, 0.5, 0.75, 1.0), then this round value is taken, otherwise the average of moon phases for the start of the day and the end of the day is taken summary |
| `temp` | [`Temp`](../../doc/models/temp.md) | Optional | Units – default: kelvin, metric: Celsius, imperial: Fahrenheit. How to change units used |
| `feels_like` | [`FeelsLike`](../../doc/models/feels-like.md) | Optional | This accounts for the human perception of weather. Units – default: kelvin, metric: Celsius, imperial: Fahrenheit. How to change units used |
| `pressure` | `float` | Optional | Atmospheric pressure on the sea level, hPa |
| `humidity` | `float` | Optional | Humidity, % |
| `dew_point` | `float` | Optional | Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form. Units – default: kelvin, metric: Celsius, imperial: Fahrenheit. |
| `uvi` | `float` | Optional | UV index |
| `clouds` | `float` | Optional | Cloudiness, % |
| `wind_speed` | `float` | Optional | Wind speed. Units – default: metre/sec, metric: metre/sec, imperial: miles/hour.How to change units used |
| `wind_gust` | `float` | Optional | (where available) Wind gust. Units – default: metre/sec, metric: metre/sec, imperial: miles/hour. How to change units used |
| `wind_deg` | `float` | Optional | Wind direction, degrees (meteorological) |
| `pop` | `float` | Optional | Probability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100% |
| `rain` | [`DailyRain`](../../doc/models/daily-rain.md) | Optional | Minute weather measurements |
| `snow` | [`DailySnow`](../../doc/models/daily-snow.md) | Optional | Minute weather measurements |
| `weather` | [`List[DailyWeather]`](../../doc/models/daily-weather.md) | Optional | current weather details |

## Example (as JSON)

```json
{
  "dt": 1706760000.0,
  "sunrise": 1706741791.0,
  "sunset": 1706778792.0,
  "moonrise": 1706800980.0,
  "moonset": 1706752680.0,
  "moon_phase": 0.69,
  "pressure": 1033,
  "humidity": 63,
  "dew_point": 263.8,
  "uvi": 2.1,
  "clouds": 60,
  "wind_speed": 13.89,
  "wind_gust": 14.66,
  "wind_deg": 16,
  "pop": 0
}
```

