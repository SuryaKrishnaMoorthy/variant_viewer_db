# Standard Libraries
import json

# External Libraries
import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'],
                        max_content_width=80)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def cli():
    pass


@cli.command()
@click.option('--verbose', '-v',
              is_flag=True,
              help='Include all metadata.')
@click.argument('name')
def hello(name, verbose):
    """Command for greeting an individual.  The output can be
    formatted with Python's JSON tool for readability:

    cliapp hello [OPTIONS] NAME | python -m json.tool

    \b
    Args:
        name (str): name of...
        verbose (flag): print additional info...
    \b
    Returns:
        greeting (JSON): JSON string with greeting
    """

    data = {
        'name': name,
        'verbose': verbose,
        'greeting': f'Hello, {name}!',
    }

    click.echo(json.dumps(data))
