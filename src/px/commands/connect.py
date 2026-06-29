import os
import subprocess
import typer

from px.core.psql import build_psql_command
from px.core.explain import explain_flags

SEPARATOR = "-" * 60


def run_connect():
    typer.echo("px → connect to postgres\n")

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

    raw_db = typer.prompt(
        "Database (optional)",
        default="",
        show_default=False
    )

    # ✅ env + fallback logic
    user = raw_user or os.getenv("PGUSER") or "postgres"
    env_host = os.getenv("PGHOST")
    host = raw_host or env_host or "localhost"

    port = (
        int(raw_port)
        if raw_port
        else int(os.getenv("PGPORT")) if os.getenv("PGPORT") else None
    )

    db = raw_db or os.getenv("PGDATABASE")

    include_host = bool(raw_host or env_host)

    cmd = build_psql_command(host, user, db, port, include_host)

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