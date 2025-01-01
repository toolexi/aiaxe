import click
from components._requests_handler import start_components

@click.group()
def cli():
    """AiAxe cli"""
    pass

@click.command()
@click.argument("start")
def cli(start):
    start_components()