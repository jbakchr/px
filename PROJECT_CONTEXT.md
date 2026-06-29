# px – Project Context

## 🧠 What this project is

px is a small CLI tool that helps me use `psql` without having to remember its flags.

The focus is NOT:

- to abstract PostgreSQL
- to replace `psql`
- to build a full-featured database tool

The focus is:
✅ using `psql` through guided prompts

---

## 🎯 Core philosophy

The goal is not:

- to hide complexity
- to simplify everything away
- to avoid learning `psql`

The goal is:
✅ to make `psql` easier to use through repetition

Success is measured by:

- Do I recognize common `psql` flags?
- Do I understand what they do?
- Do I rely less on px over time?

---

## ⚡ Key realization (important)

px should NOT replace `psql`.

Instead, it should:
✅ expose the real `psql` command  
✅ explain it  
✅ reinforce it through use

The biggest risk is not:
❌ missing features

The biggest risk is:
❗ overengineering and losing simplicity

---

## 🔁 Current learning loop

px currently supports a single, focused loop:

### 🔹 Connect loop

```

px c
→ answer prompts (user, host, port, database)
→ see generated command
→ understand flags
→ run real psql
→ interact with database
→ exit
→ repeat

```

What this reinforces:

- connection patterns
- common flags
- mental model of accessing a database

---

## 🧪 Current state

px currently supports:

- ✅ px c (connect)
- ✅ interactive prompts
- ✅ real `psql` execution
- ✅ command visibility (👉 psql ...)
- ✅ flag explanations (“what + why”)
- ✅ conditional flag inclusion (only when relevant)
- ✅ minimal and predictable flow

---

## ✅ UX (important)

The experience is intentionally simple:

- ✅ minimal context header:

```

px → connect to postgres

```

- ✅ clear command visibility:

```

👉  psql -U postgres -h localhost -p 5432

```

- ✅ structured explanation:

```

-U → database user
(who you connect as)

```

- ✅ relevant prompts only
- ✅ clean separators for readability
- ✅ real `psql` session takes over (not hidden)

👉 UX is part of the learning system

---

## 🧠 Core concept (important)

The most important idea in px:

```

Prompt → Build → Show → Explain → Execute

```

This creates a simple learning loop:

- see the command
- understand the flags
- run it
- repeat

---

## 🧠 Core learning model (important)

px encourages learning through repetition of:

```

psql
→ -U (user)
→ -h (host)
→ -p (port)
→ -d (database)

```

Key idea:

- flags are introduced _in context_
- explanations are short and practical
- behavior is predictable

👉 builds pattern recognition over time

---

## 🔍 Key insights so far

- ✅ Seeing the real command is critical
- ✅ Explaining flags reinforces understanding
- ✅ Too many prompts = friction
- ✅ Simplicity beats completeness
- ✅ Defaults reduce cognitive load
- ✅ Conditional flags improve clarity
- ✅ Repetition builds intuition
- ✅ UX structure affects learning
- ✅ Showing omissions (e.g. no `-h`) improves understanding

---

## 🧭 Intended direction (high level)

px evolves from:

"help me connect to Postgres"

to:

"help me feel comfortable using `psql`"

But always within a **very narrow scope**

---

## 🧱 Near-term evolution priorities

### 1. Reduce friction (highest value)

- Improve prompt wording
- Reduce unnecessary input
- Use sensible defaults
- Keep flow fast

---

### 2. Improve learning clarity

- Refine flag explanations
- Show omitted flags when relevant
- Keep explanations:
  - short
  - consistent
  - practical

---

### 3. Maintain simplicity

- Avoid adding too many commands
- Avoid abstraction layers
- Keep everything predictable

---

## 🔄 Structural direction (important)

From:
"generate a command"

To:
"guide a simple interaction with `psql`"

This is the shift from:

a helper script  
to:  
✅ a focused learning tool

---

## 🚫 Non-goals

- Not a full PostgreSQL client
- Not a replacement for `psql`
- Not a generic CLI framework
- Not feature-complete
- Not an automation tool

---

## ✅ What makes this project different

This is not:

- a database management tool
- a GUI replacement
- a productivity optimizer

This is:
✅ a minimal CLI helper for `psql`

Designed to:

- reduce friction
- expose real commands
- reinforce understanding
- build confidence over time

---

## 🧠 Why this matters (personally)

This project helps:

- avoid repeatedly looking up `psql` flags
- move from guessing → understanding
- reduce mental overhead when connecting to databases
- build confidence with PostgreSQL CLI usage

It is both:

- a practical tool
- a learning aid

---

## 🚀 What I want help with in a new chat

- Evolve px step-by-step
- Keep everything minimal and focused
- Improve clarity without adding complexity
- Reduce friction in the connect flow
- Reinforce learning through repetition

---

## 💡 How to use this context

When starting a new chat, say:

```

I’m working on this project:
[paste PROJECT_CONTEXT.md]

I want help evolving it step-by-step without overengineering.

Let’s start with [X]

```
