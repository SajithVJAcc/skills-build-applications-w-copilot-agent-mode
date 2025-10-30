## Purpose

This file gives focused, actionable instructions for AI coding agents (Copilot/agent mode) to be immediately productive in this repository. It summarizes the project's high-level architecture, developer workflows, and repository-specific conventions discovered in `README.md`, `docs/octofit_story.md`, and `.github/instructions/*.instructions.md`.

## Big picture (what this repo contains)

- This is a workshop/exercise repository for the "OctoFit Tracker" app. The intended app layout is `octofit-tracker/` with two main components:
  - `octofit-tracker/backend/` — Django REST API (Python)
  - `octofit-tracker/frontend/` — React.js frontend
- Persistent layer: MongoDB accessed via `djongo`/`pymongo`. The project uses Django ORM wrappers; prefer ORM usage over raw Mongo scripts.

## Key, discoverable files to consult

- `README.md` — project overview and high-level goals.
- `docs/octofit_story.md` — product story and feature list (useful for UX/feature context).
- `.github/instructions/*.instructions.md` — contains workspace-specific rules (very important). Examples:
  - `.github/instructions/octofit_tracker_setup_project.instructions.md` — setup rules (venv, requirements file path).
  - `.github/instructions/octofit_tracker_django_backend.instructions.md` — Django-specific snippets and required settings.
  - `.github/instructions/octofit_tracker_react_frontend.instructions.md` — React setup commands and image location.

When unsure about a convention, check those `.github/instructions/*` files first — they encode explicit agent rules.

## Project-specific conventions and rules (must-follow)

- Never change directories when running commands in agent mode: always pass full/relative target paths (e.g., `python3 -m venv octofit-tracker/backend/venv`).
- Forwarded ports (only these):
  - 8000 (public) — Django
  - 3000 (public) — React dev server
  - 27017 (private) — MongoDB
  Do not propose other ports to forward.
- Python virtualenv location: `octofit-tracker/backend/venv` and install via:

  python3 -m venv octofit-tracker/backend/venv
  source octofit-tracker/backend/venv/bin/activate
  pip install -r octofit-tracker/backend/requirements.txt

- Frontend setup must use `--prefix` to install into the frontend folder. Examples from the instructions:

  npx create-react-app octofit-tracker/frontend --template cra-template --use-npm
  npm install bootstrap --prefix octofit-tracker/frontend
  npm install react-router-dom --prefix octofit-tracker/frontend

  (Also: add Bootstrap import to `octofit-tracker/frontend/src/index.js`.)

## Django / Backend conventions

- `settings.py` must include `ALLOWED_HOSTS` handling that adds Codespace host when `CODESPACE_NAME` exists. Follow the pattern in `.github/instructions/octofit_tracker_django_backend.instructions.md`.
- `urls.py` should construct a `base_url` using `CODESPACE_NAME` if present; the API root and router are used for endpoints. Use the same pattern in new services/endpoints.
- Use Django serializers that convert MongoDB ObjectId fields to strings (serializers should coerce ObjectId -> str).
- Always prefer Django ORM (or djongo ORM-level usage), not raw direct mongo scripts, for creating DB schema/data.

## Quick examples (where to add code)

- New API endpoint:
  - Add serializer in `octofit-tracker/backend/<app>/serializers.py` following ObjectId->string policy.
  - Add viewsets in `octofit-tracker/backend/<app>/views.py` and register them with the DRF router in `urls.py`.

- New frontend component:
  - Place React components under `octofit-tracker/frontend/src/components/` and add routes with `react-router-dom`.
  - Use the project image at `docs/octofitapp-small.png` for UI mocks.

## Integration notes & dependencies

- The backend uses `djongo` + `pymongo` (see `.github/instructions` listing required packages). Ensure new code considers Mongo's ObjectId semantics.
- Tests are not provided in the repository by default — prefer small, focused local smoke tests using `curl` against `http://localhost:8000` or the Codespace URL pattern when `CODESPACE_NAME` is set.

## What to do when making changes (agent checklist)

1. Check `.github/instructions/*.instructions.md` for any hard rules that apply to your change.
2. When running commands, never `cd` — use explicit paths.
3. Use only the allowed forwarded ports (8000, 3000, 27017).
4. For backend changes: follow the `ALLOWED_HOSTS` and `urls.py` Codespace pattern and ensure serializers convert `ObjectId` to `str`.
5. For frontend changes: use `--prefix octofit-tracker/frontend` when running `npm` commands.

## When you need clarification

- If a rule conflicts with a needed change (for example, port or path), stop and ask the maintainer — do not override repository .instructions files.

---
If you'd like, I can now merge this into `.github/copilot-instructions.md` (or update an existing file) and adapt wording for a specific agent persona (e.g., stricter Codespace rules or broader local dev guidance). What would you prefer?
