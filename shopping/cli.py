import click
from .core import greet


@click.group()
def main():
    """Shopping CLI"""
    pass


@main.command(name="greet")
@click.option("--name", "-n", default="World", help="Name to greet")
def greet_cmd(name: str):
    """Print a greeting."""
    click.echo(greet(name))


if __name__ == "__main__":
    main()
