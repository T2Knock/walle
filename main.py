import os
import click


@click.group()
def cli():
    pass


@cli.command()
def sync():
    wallpaper_path = os.path.join(os.getcwd(), "images")
    for file in os.listdir(wallpaper_path):
        file_name = os.path.splitext(file)
        print(file_name[0])


if __name__ == "__main__":
    cli()
