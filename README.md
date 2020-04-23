# Weather

This is a terminal application to check the weather using
[Open Weather API](https://openweathermap.org).

## Development Status

As of April 23, 2020: `Development Status :: 3 - Alpha`. 

## Installation

```bash
# enter project root, check wheel installation
python -m pip install --user wheel
# build wheel and install weather
python setup.py bdist_wheel
python -m pip install --user -r requirements.txt
```

## Notes

Add `forecast` function to script, e.g.

```python
# Query for 3 hours weather forecast for the next 5 days over toponym
forecast = owm.three_hours_forecast(toponym).get_forecast()
weathers = forecast.get_weathers()
for weather in weathers:
    print(weather.get_status())
```

The free API limits forecasts to three hours into the future.

## TODO

Add customization:

- [ ] Set configuration in the terminal
- [ ] Add more units for temperature results: `[ 'kelvin', 'fahrenheit', 'celsius' ]`.
- [ ] Edit `color_temperature()` in `utils.py` for the other two units.
- [ ] Add `German` and `Japanese` as locals
- [ ] Add screenshot and documentation
