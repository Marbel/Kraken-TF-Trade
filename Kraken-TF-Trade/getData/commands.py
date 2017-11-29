import click
import urllib.request
import json
from configparse import Config
import database
import datetime
import krakenex
import time


@click.command()
def getallloggedinuserdata():
    """Get the last 24h of data from loggedin users in steam"""
    # Get Steam User statistics
    jsoncontent = urllib.request.urlopen("http://store.steampowered.com/stats/userdata.json").read()
    content = json.loads(jsoncontent)[0]
    datapoints = content['data']

    # start database connection
    database.db_connect()
    # deactivate autocommit so script can save the files faster
    database.database.set_autocommit(False)
    database.database.begin()
    for datapoint in datapoints:
        userdate = datetime.datetime.utcfromtimestamp(float(datapoint[0]) / 1000.)
        try:
            userlogged = database.UserLoggedIn.create(time=userdate, userloggedin=datapoint[1])
        except Exception as e:
            continue
    database.database.commit()
    # activate autocommit
    database.database.set_autocommit(True)
    # close database connection
    database.db_close()


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
