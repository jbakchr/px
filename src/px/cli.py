import typer
from px.commands.connect import run_connect

app = typer.Typer()


@app.command(name="c")
def connect_short():
    run_connect()


@app.command()
def connect():
    run_connect()


def main():
    app()


if __name__ == "__main__":
    main()