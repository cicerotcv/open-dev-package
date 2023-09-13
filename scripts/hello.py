#!/usr/bin/env python3
import gettext

from dev_aberto.dev_aberto import hello
from babel.dates import format_date
from datetime import datetime

gettext.install("cli", localedir="locale")


if __name__ == "__main__":
    date, name = hello()
    parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    print(_("last_commit_at"), format_date(parsed_date), _("by"), name)
