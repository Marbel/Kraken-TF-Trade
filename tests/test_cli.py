import pytest
from click.testing import CliRunner
from Kraken - TF - Trade import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hello.'


def test_cli_with_arg(runner):
    result = runner.invoke(cli.version)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == '0.0.1'
