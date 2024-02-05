# Current

Get current weather details

```python
current_controller = client.current
```

## Class Name

`CurrentController`


# Current Weather Data

Get the current weather info

```python
def current_weather_data(self,
                        lat,
                        lon,
                        exclude=None,
                        units=None,
                        lang=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lat` | `float` | Query, Required | Latitude, decimal (-90; 90). If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use our Geocoding API |
| `lon` | `float` | Query, Required | Longitude, decimal (-180; 180). If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use our Geocoding API |
| `exclude` | `str` | Query, Optional | By using this parameter you can exclude some parts of the weather data from the API response. It should be a comma-delimited list (without spaces). |
| `units` | [`UnitsEnum`](../../doc/models/units-enum.md) | Query, Optional | Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default. |
| `lang` | [`LangEnum`](../../doc/models/lang-enum.md) | Query, Optional | You can use the lang parameter to get the output in your language. |

## Response Type

[`WeatherInfo`](../../doc/models/weather-info.md)

## Example Usage

```python
lat = 37.8349

lon = 122.1297

exclude = 'hourly,minutely'

units = UnitsEnum.IMPERIAL

lang = LangEnum.EN

result = current_controller.current_weather_data(
    lat,
    lon,
    exclude=exclude,
    units=units,
    lang=lang
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found response | `APIException` |

