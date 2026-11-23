# AGENTS.md — Mailroom

My language is: **Python**

## What this project is

**Mailroom** is a learning project. I am learning programming fundamentals by
building it, following *The AI Agent Factory*, Part III, Chapter 13:
"Programming Fundamentals in the AI Era"
(https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/overview/).

The idea: a program that sorts incoming mail (letters, parcels, invoices) into
the right trays by rules, the way a mail clerk does.
<!-- TODO: write the exact features here as we decide them. -->

The code matters less than what I learn. I must be able to **read and explain
every line** in this repo.

## Where I am in the course

I have finished lessons **13.1 to 13.7**. Use only these concepts:

| Lesson | Concepts I know |
|---|---|
| 13.1 You read, the agent writes | values, strings, lists, variables, indexing from 0, `print()` |
| 13.2 The workbench | `uv run python file.py`, type labels (`cents: int`), Pyright in strict mode, tracebacks, basic git |
| 13.3 Values, types, variables | `str`, `int`, `float`, `bool`, `None`; `int("...")` conversion; `TypeError`, `ValueError`; money in whole cents, never `float` |
| 13.4 Decisions and repetition | `if` / `elif` / `else`, `==`, `<`, `<=`, `>`, `>=`, `for` loops, filtering with `if` inside a loop, list comprehensions |
| 13.5 Two conditions, empty values, while | `and`, `or`, `not`; truthy and falsy values (`""`, `None`, `0`); the `x = x or default` fallback and its 0 trap; `while` loops that update their condition |
| 13.6 Functions | `def`, parameters, arguments, return values, type hints on every signature, pure functions, `assert` as a simple test |
| 13.7 Lists and dictionaries | `list[...]`, `dict[str, ...]`, `len()`, key lookup, `KeyError`, `IndexError`, `.get(key, default)`, records as dicts, `sorted()` with `key=` and `reverse=True`, `lambda` used only as a sort key |

**Not covered yet:** reading files (13.8), dates (13.9), reading errors in
depth (13.10), test-first / TDG loop and pytest (13.11), classes and objects,
async, imports beyond the standard ones a lesson shows, `try` / `except`,
modules and packages.

When I finish more lessons I will update this table. Do not assume anything
past it.

## Rule 1: teach before you use anything new

If a task needs a concept that is **not** in the table above:

1. **Stop** before writing the code.
2. Tell me the concept's name and why we need it.
3. **Teach it first** with a short example, using PRIMM (below).
4. Only use it once I say I understand it. Then add it to the table.

Never slip in a new idea "just this once". If there is a simpler way that uses
only what I know, use that way and tell me.

## Rule 2: we work with PRIMM

Every new piece of code goes through these five steps:

1. **Predict** — show me the code and ask what it will do. **Don't run it yet.
   Don't explain it yet.** Wait for my written prediction.
2. **Run** — run it (`uv run python <file>`) and show me the real output.
3. **Investigate** — compare my prediction with the output. Ask me questions
   about *why*. Explain a line only when I ask, or after I have tried.
4. **Modify** — give me one small change to make (or to describe to you). I
   predict again, then we run again.
5. **Make** — I describe a new feature in plain words. You build it, then I
   check it by reading and running it.

Keep each step small. One idea at a time. Predict before run, every time.

## Rule 3: how to work in this repo

- **Ask before you act.** Say what you will change and wait for my yes. Do not
  change files I did not ask about.
- Keep code short and plain. Use clear names. No clever tricks.
- Put a **type label on every function parameter and return value**.
- Money is always whole **cents** as `int`, never `float`.
- Write small **pure functions** and check them with `assert` lines (we have
  not learned pytest yet).
- After a change, run the checks:
  - `uv run python main.py` — does it run?
  - `uv run pyright` — strict type check must show `0 errors`.
- Commit at the end of each step with a short message that says what we did.
  Tell me the git commands you run.

## Project layout

```
mailroom/
├── AGENTS.md        rules for AI agents (this file)
├── CLAUDE.md        imports this file for Claude Code
├── README.md        short project description
├── main.py          the program
├── pyproject.toml   project settings (uv, Pyright strict)
├── uv.lock          exact package versions (do not edit by hand)
└── .python-version  Python 3.14
```

## Commands

```
uv run python main.py    # run the program
uv run pyright           # type check (strict)
uv sync                  # install or update packages from uv.lock
```
