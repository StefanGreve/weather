#!/usr/bin/env python3

import utils
from datetime import date

import pyowm
import click

def print_version(ctx, param, value):
    meta = utils.read_json(utils.path_settings('weather').joinpath('meta.json'))

    if not value or ctx.resilient_parsing:
        return

    click.secho(f"\nPython {meta['name']} version {meta['version']}", fg = 'yellow')
    click.echo(f"Copyright (C) {date.today().year} {meta['author']}")
    click.echo("License GPLv3: GNU GPL version 3 <https://gnu.org/licenses/gpl.html>")
    click.echo("This is free software: you are free to change and redistribute it.")
    click.echo("There is NO WARRANTY, to the extent permitted by law.\n")
    ctx.exit()

@click.group()
@click.option('--verbose', '-V', is_flag = True, help = "Enable verbose mode for invocations.")
@click.option('--version', is_flag = True, callback = print_version, expose_value = False, is_eager = True, help = "Display package version information.")
@click.option('--unit', default = 'celsius', type = click.Choice(['celsius', 'fahrenheit', 'kelvin'], case_sensitive = False), help = "Set temperature unit.")
@click.pass_context
def cli(ctx, verbose, unit):
    ctx.ensure_object(dict)
    ctx.obj['PROJECT'] = "weather"
    ctx.obj['META'] = utils.path_settings(ctx.obj['PROJECT']).joinpath('meta.json')
    ctx.obj['SETTINGS'] = utils.path_settings(ctx.obj['PROJECT']).joinpath('settings.json')
    ctx.obj['API_KEY'] = utils.read_json(ctx.obj['SETTINGS'])['API_KEY']
    ctx.obj['VERBOSE'] = verbose
    ctx.obj['UNIT'] = unit

@cli.command()
@click.argument('toponyms', nargs = -1)
@click.pass_context
def today(ctx, toponyms):
    settings = utils.read_json(ctx.obj['SETTINGS'])
    unit = ctx.obj['UNIT']

    if not toponyms:
        click.secho("Error: Toponym is undefined.", err = True, fg = 'red')

    owm = pyowm.OWM(settings['API_KEY'])

    for toponym in toponyms:
        observation = owm.weather_at_place(toponym)
        weather = observation.get_weather()
        observation_date = observation.get_reception_time(timeformat = 'date')
        temperature = weather.get_temperature(unit)
        set_temp_string = lambda tmp: utils.set_temp_string(tmp, unit)

        if ctx.obj['VERBOSE']:
            click.echo("\nWeather Forecast")
            click.echo(f"On {observation_date.strftime('%B %d, %Y')} at {observation_date.strftime('%I:%M %p')}")
            click.echo(f"In {observation.get_location().get_name()} ({observation.get_location().get_lat()},{observation.get_location().get_lon()})\n")
            click.echo(f"Status\t\t{weather.get_detailed_status()}")
            click.echo(f"minTemp\t\t{utils.color_temperature(temperature['temp_min'], set_temp_string(temperature['temp_min']), unit)}")
            click.echo(f"nowTemp\t\t{utils.color_temperature(temperature['temp'], set_temp_string(temperature['temp']), unit)}")
            click.echo(f"maxTemp\t\t{utils.color_temperature(temperature['temp_max'], set_temp_string(temperature['temp_max']), unit)}")
            click.echo(f"Wind Speed\t{weather.get_wind()['speed']}m/s")
            click.echo(f"Humidity\t{weather.get_humidity()}%")
            click.echo(f"Cloud Coverage\t{weather.get_clouds()}%")
            click.echo(f"Atm. Pressure\t{weather.get_pressure()['press']} hpa\n")
        else:
            click.echo(utils.status_to_emoji(weather.get_status()), nl = False)
            click.echo(f"  {utils.color_temperature(temperature['temp'], set_temp_string(temperature['temp']), unit)} ", nl = False)
            click.echo(f"{click.style('[ ', fg = 'magenta')}", nl = False)
            click.echo(observation_date.strftime('%B %d'), nl = False)
            click.echo(f"{click.style(' ]', fg = 'magenta')} ", nl = False)
            click.echo(f"@ {observation_date.strftime('%I:%M %p')}")

if __name__ == '__main__':
    try:
        cli(obj = {})
    except KeyboardInterrupt:
        pass
