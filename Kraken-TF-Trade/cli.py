import click
import configparse
import krakenex

from getData import commands as getDataGroup
from exportData import commands as exportDataGroup


@click.group()
def cli():
    pass


@cli.command()
def main():
    """A Kraken Trade bot which use tensorflow to predict price changes"""
    greet = 'Hello'
    click.echo('{0}.'.format(greet))


@cli.command()
def version():
    """Display the current version."""
    click.echo(_read_version())


cli.add_command(getDataGroup.currencies)
cli.add_command(getDataGroup.currency_info)
cli.add_command(getDataGroup.currency_trades)
# cli.add_command(exportDataGroup.command_group)


if __name__ == '__main__':
    cli()
