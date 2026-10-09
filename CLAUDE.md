# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

`move37` — a minimal Django app. `/` serves a greeting (default "Hello, human"); the greeting is editable in the Django admin at `/admin/`.

## Commands

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # for /admin/
python manage.py runserver
python manage.py test
```

## Architecture

- `config/` — Django project (settings, root URLs).
- `hello/` — app with a `Greeting` model (registered in admin) and an `index` view that returns the latest active greeting, falling back to "Hello, human".
- SQLite database (`db.sqlite3`, gitignored).

## Conventions

- Develop on a feature branch; do not push directly to the default branch.
- Keep commits small with descriptive messages.
- Open a pull request for review; don't open one unless asked.
- Match the style of surrounding code (naming, comment density, idiom).
