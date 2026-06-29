import typer


def explain_flags(include_host, user, db, port):
    if user:
        typer.echo("-U → database user")
        typer.echo("     (who you connect as)\n")

    if include_host:
        typer.echo("-h → database host")
        typer.echo("     (where your database is running)\n")

    if port:
        typer.echo("-p → port")
        typer.echo("     (how to reach the database service)\n")

    if db:
        typer.echo("-d → database name")
        typer.echo("     (which database to use)\n")