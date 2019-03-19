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
def hello():
    click.echo("hello world")
