# px

> A minimal CLI on top of `psql`.

px is a small command-line tool that helps you **connect to PostgreSQL without remembering `psql` flags**.

It guides you through the required inputs, shows the generated command, explains the flags, and then executes it.

---

## 🧠 Why px?

I kept forgetting how to connect to Postgres:

```

psql -U user -h host -p port -d db

```

So instead of looking it up every time, I built px.

px turns:

❌ "What were those flags again?"

into

✅ "Just follow the prompts"

---

## ⚡ Features (current)

### `px c` → connect to Postgres

- Prompts for user, host, port, and database
- Builds the correct `psql` command
- Explains each flag
- Executes it

---

## 🖥 Example

```

$ px c

px → connect to postgres

User (default: postgres):
Host (optional: localhost):
Port (optional: 5432):
Database (optional):

***

Generated command:

👉  psql -U postgres -h localhost -p 5432

Explanation:

-U → database user
(who you connect as)

-h → database host
(where your database is running)

-p → port
(how to reach the database service)

***

Executing psql...

```

---

## 🧩 Design

px follows a simple flow:

```

Prompt → Build → Show → Explain → Execute

```

It’s not meant to replace `psql`, but to make using it **easier and more repeatable**.

---

## 🛠 Installation

Clone the repo and install in editable mode:

```

pip install -e .

```

Then run:

```

px c

```

---

## 📦 Requirements

- Python 3.9+
- `psql` installed and available in your PATH

---

## 🎯 Scope

px is intentionally narrow.

It is **only focused on improving the `psql` experience**, not building a general command framework.

---

## 🚀 Future (possible additions)

- More `psql`-related flows (e.g. switching databases, running queries)
- Small improvements to the connect experience

All additions will stay:

- simple
- focused
- specific to PostgreSQL

---

## 🗂 Project Structure

```

src/
  px/
    cli.py

```

---

## 🧠 Insight

You don’t need to remember `psql`.

You just need to use it.

## License

MIT
