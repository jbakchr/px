# px - ROADMAP

> Small improvements to reduce friction when using `psql`

This project evolves through small, focused steps.
Each feature should:

- reduce friction
- reinforce usage
- stay minimal

---

## ✅ Done

- [x] `px c` → connect to postgres
  - prompts for user, host, port, database
  - builds command
  - explains flags
  - executes

---

## 🔜 Next

### 1. Default connection profiles

Store commonly used configs:

```

px c --profile local
px c --profile prod

```

Goal:

- avoid retyping common values
- still allow overrides

---

### 2. Environment variable support

Automatically use:

```

PGHOST
PGUSER
PGPORT
PGDATABASE

```

Goal:

- integrate with existing setups
- reduce prompts when values already exist

---

### 3. Dry-run mode

```

px c --dry-run

```

Goal:

- show command without executing
- useful for learning / verification

---

### 4. Explain full command (always)

Always show all possible flags, even if omitted:

Example:

```

-h omitted
(using local socket)

```

Goal:

- improve understanding of defaults and behavior

---

## 🔧 Nice to have

### 5. Quick reconnect

```

px rc

```

Reconnect using last used parameters

Goal:

- fast iteration during development

---

### 6. Connection string support

```

px c --url postgres\://user\@host:5432/db

```

Goal:

- support common format
- still explain parsed flags

---

### 7. Run single query

```

px q

```

Flow:

- prompt for query
- build:

```

psql -c "<query>"

```

- explain `-c`

Goal:

- quick queries without entering interactive mode

---

### 8. List databases

```

px ls

```

Runs:

```

\l

```

Goal:

- expose common psql actions in guided way

---

## ❌ Out of scope (for now)

- non-psql commands (git, docker, etc.)
- complex abstractions
- configuration-heavy systems
- plugins / frameworks

---

## 🧠 Guiding principle

px is not trying to replace `psql`.

It exists to make `psql`:

- easier to use
- easier to learn
- easier to repeat

---

## ✅ Definition of done (for each feature)

- prompts are clear
- command is visible
- flags are explained
- behavior is predictable
- no unnecessary complexity added
