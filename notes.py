import click
import crud
@click.group()

def cli()->None:
    print("I'm running!")


@cli.command()

def new_command():
    pass

cli.add_command(crud.create)