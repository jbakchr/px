import typer


def explain_flags(include_host, user, db, port):
    included = []
    omitted = []

    # ✅ -U (always included)
    included.append((
        "-U",
        "database user",
        "(who you connect as)"
    ))

    # ✅ -h
    if include_host:
        included.append((
            "-h",
            "database host",
            "(where your database is running)"
        ))
    else:
        omitted.append((
            "-h",
            "database host",
            "(using environment/default)"
        ))

    # ✅ -p
    if port:
        included.append((
            "-p",
            "port",
            "(how to reach the database service)"
        ))
    else:
        omitted.append((
            "-p",
            "port",
            "(using default behavior)"
        ))

    # ✅ -d
    if db:
        included.append((
            "-d",
            "database name",
            "(which database to use)"
        ))
    else:
        omitted.append((
            "-d",
            "database name",
            "(not specified)"
        ))

    # ✅ render output

    if included:
        typer.echo("Included flags:\n")
        for flag, title, desc in included:
            typer.echo(f"{flag} → {title}")
            typer.echo(f"     {desc}\n")

    if omitted:
        typer.echo("Omitted flags:\n")
        for flag, title, desc in omitted:
            typer.echo(f"{flag} → {title}")
            typer.echo(f"     {desc}\n")
