import subprocess
import typer

app = typer.Typer()

SEPARATOR = "-" * 60


def build_psql_command(host, user, db, port, include_host):
    cmd = ["psql"]

    if user:
        cmd += ["-U", user]

    if include_host:
        cmd += ["-h", host]

    if db:
        cmd += ["-d", db]

    if port:
        cmd += ["-p", str(port)]

    return cmd


def explain_flags(include_host, user, db, port):
    if user:
        typer.echo("-U → database user")
        typer.echo("     (who you connect as)\n")

    if include_host:
        typer.echo("-h → database host")
        typer.echo("     (where your database is running)\n")

    if db:
        typer.echo("-d → database name")
        typer.echo("     (which database to use)\n")

    if port:
        typer.echo("-p → port")
        typer.echo("     (how to reach the database service)\n")


@app.command(name="c")
def connect_short():
    connect()


@app.command()
def connect():
    typer.echo("px → connect to postgres\n")

    # ✅ prompts (clean, explicit defaults)
    raw_user = typer.prompt(
        "User (default: postgres)",
        default="",
        show_default=False
    )

    raw_host = typer.prompt(
        "Host (optional: localhost)",
        default="",
        show_default=False
    )

    raw_port = typer.prompt(
        "Port (optional: 5432)",
        default="",
        show_default=False
    )

    db = typer.prompt(
        "Database (optional)",
        default="",
        show_default=False
    )

    # ✅ apply defaults
    user = raw_user or "postgres"
    host = raw_host or "localhost"
    port = int(raw_port) if raw_port else None

    # ✅ only include host if explicitly typed
    include_host = bool(raw_host)

    cmd = build_psql_command(host, user, db, port, include_host)

    # ✅ structured output (dx-style)
    typer.echo("\n" + SEPARATOR + "\n")

    typer.echo("Generated command:\n")
    typer.echo("👉  " + " ".join(cmd) + "\n")

    typer.echo("Explanation:\n")
    explain_flags(include_host, user, db, port)

    typer.echo(SEPARATOR + "\n")

    typer.echo("Executing psql...\n")

    try:
        subprocess.run(cmd)
    except FileNotFoundError:
        typer.echo("❌ psql not found. Make sure it is installed.")


def main():
    app()


if __name__ == "__main__":
    main()