# PostgreSQL configuration

Set `KONTAKT_DB_USER` and `KONTAKT_DB_PASSWORD` in the process environment before launching `python main.py` from the repository root. Optional settings and defaults are listed in [`.env.example`](../.env.example). The example is a reference, not an automatically loaded configuration file.

An empty or missing username/password raises a clear error before connecting. SQLAlchemy builds the URL so special characters in credentials are encoded correctly. The driver remains psycopg2; ensure it is installed.

Use a dedicated demonstration database: the pipeline replaces the `users` table. This change does not modify that existing behavior.

No credentials belong in committed code or documentation. Removing a value from the current file does not remove it from Git history. If a previously committed password is real or reused, change it at the database before relying on this cleanup.
