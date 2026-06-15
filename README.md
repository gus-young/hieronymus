# Hieronymus

> *"In the Garden of Earthly Delights, everyone is already working on something."*

Hieronymus (Hiro for short) is a multi-agent coding system that turns a project idea into a running codebase. Tell it what you want to build. It interviews you until it understands the project well enough to decompose it into a dependency graph, spins up a crew of worker agents, and builds it -- in parallel where possible, in sequence where it has to be.

Named after Hieronymus Bosch, whose paintings depict dozens of figures all doing their own chaotic work simultaneously. That's the architecture.

---

## How It Works

```
You describe an idea
        |
        v
Hiro (PM agent) asks clarifying questions -- one at a time
        |
        v
Recommends a tech stack for your approval
        |
        v
Presents a requirements summary -- you confirm or revise
        |
        v
Decomposes the project into a dependency-aware task graph
        |
        v
Spawns worker agents for independent tasks in parallel
        |
        v
Human-in-the-loop checkpoints before merging work
        |
        v
Working code in a GitHub repo, tasks tracked as issues
```

---

## Status

- [x] Stage 1 -- PM agent (requirements gathering, task decomposition)
- [ ] Stage 2 -- Worker agents (code generation, self-testing)
- [ ] Stage 3 -- GitHub integration (repo creation, issues, branches)
- [ ] Stage 4 -- Parallel execution (asyncio worker pool)
- [ ] Stage 5 -- Token budget tracking and pause/resume

---

## Quickstart

```bash
git clone https://github.com/gus-young/hieronymus
cd hieronymus
pip install -r requirements.txt
cp .env.example .env  # add your ANTHROPIC_API_KEY
uvicorn app:app --reload
```

Open `http://localhost:8000` and describe what you want to build.

---

## Tech Stack

- **Backend:** FastAPI + Python
- **Agent:** Anthropic API (Claude Sonnet)
- **Structured outputs:** Pydantic
- **Frontend:** Vanilla JS (no framework -- it's a chat window, not a SPA)
- **Storage:** JSON files (simple on purpose -- Stage 2 will revisit this)

---

## Project Layout

```
hieronymus/
  app.py            # FastAPI entry point and routes
  agent/
    pm_agent.py     # PMAgent class -- the orchestrator
    prompts.py      # All prompt templates
    models.py       # Pydantic schemas for task graph
    state.py        # Conversation state machine
  static/           # Chat UI (HTML/CSS/JS)
  outputs/          # Generated project plans (JSON)
```

---

## Philosophy

Most coding agents jump straight to writing code. Hiro doesn't. The most expensive bugs are the ones where you built the wrong thing -- and no amount of fast code generation fixes a bad spec. Hiro front-loads the thinking so the workers can move fast without second-guessing.

One question at a time. No walls of text. The agent reads the room.

---

*Built by [@gus-young](https://github.com/gus-young) as a portfolio project at the intersection of ML engineering and systems design.*
