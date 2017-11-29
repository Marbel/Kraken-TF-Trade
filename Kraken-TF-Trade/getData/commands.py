import click
import urllib.request
import json
from configparse import Config
import database
import datetime
import krakenex
import time


@click.command()
def currencies():
    """Get tradeable currencies."""
    k = krakenex.API()
    response = k.query_public('AssetPairs', data=None)
    click.echo(response)


@click.command()
@click.argument('currency')
def currency_info(currency):
    """Get currency info."""
    k = krakenex.API()
    response = k.query_public('AssetPairs', {'pair': currency})
    click.echo(response)


@click.command()
@click.argument('currency')
def currency_trades(currency):
    """Get currency trade info."""
    k = krakenex.API()
    response = k.query_public('OHLC',
                              {'pair': currency,
                               'since': str(1509494400),
                               'interval': 5})
    for datapoint in response['result'][currency]:
        click.echo(datapoint)
    # click.echo(response)
