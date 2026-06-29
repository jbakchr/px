import subprocess
import typer

app = typer.Typer()


def build_psql_command(host, user, db, port):
    cmd = ["psql"]

    if host:
        cmd += ["-h", host]
    if user:
        cmd += ["-U", user]
    if db:
        cmd += ["-d", db]
    if port:
        cmd += ["-p", str(port)]

    return cmd


def explain_flags(host, user, db, port):
    typer.echo("\n")

    if host:
        typer.echo("-h → database host")
        typer.echo("     (where your database is running)\n")

    if user:
        typer.echo("-U → database user")
        typer.echo("     (who you connect as)\n")

    if db:
        typer.echo("-d → database name")
        typer.echo("     (which database to use)\n")

    if port:
        typer.echo("-p → port")
        typer.echo("     (how to reach the database service)\n")


@app.command(name="c")
def connect_short():
    """Connect to postgres (short version)"""
    connect()


@app.command()
def connect():
    """Connect to postgres"""

    typer.echo("px → connect to postgres\n")

    host = typer.prompt("Host", default="localhost")
    user = typer.prompt("User", default="postgres")
    db = typer.prompt("Database")
    port = typer.prompt("Port (optional)", default="", show_default=False)

    port = int(port) if port else None

    cmd = build_psql_command(host, user, db, port)

    typer.echo("\n👉 " + " ".join(cmd))

    explain_flags(host, user, db, port)

    typer.echo("--- launching psql ---\n")

    try:
        subprocess.run(cmd)
    except FileNotFoundError:
        typer.echo("❌ psql not found. Make sure it is installed.")


def main():
    app()


if __name__ == "__main__":
    main()