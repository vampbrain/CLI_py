import click
from datetime import datetime
from pathlib import Path
import json
import os
from file import load, save, exists
@click.command()
@click.argument("title")
@click.option("--content", prompt=True, help = "Content of the note")
@click.option("--tags", help = "comma-separated list of tags")


def create(title: str, content: str, tags: str):
    notes_directory = Path.home()
    note_name = f"{title}.txt"

    if (notes_directory / note_name).exists():
        click.echo(f"Note with title '{title}' already exists.")
        exit(1)

    notes_data = {
        "content": content,
        "tags" : tags.split(",") if tags else[],
        "created_at": datetime.now().isoformat()

    }

    with open(notes_directory / note_name, "a+") as file:
        json.dump(notes_data, file)
    click.echo(f"Note '{title}' created.")

if __name__ == "__main__":
    create()