#!/usr/bin/env python3

from sys import (
        argv,
        exit
        )
from time import sleep

from mensa.models import db
from mensa.gui import gui
from mensa.gui import read_schild_txt

if __name__ == '__main__':
    db.bind(provider='sqlite', filename=':memory:')
    #  db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)

    gui.mainloop()

