def build_psql_command(host, user, db, port, include_host):
    cmd = ["psql"]

    if user:
        cmd += ["-U", user]

    if include_host:
        cmd += ["-h", host]

    if port:
        cmd += ["-p", str(port)]

    if db:
        cmd += ["-d", db]

    return cmd