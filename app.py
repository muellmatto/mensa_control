#!/usr/bin/env python3

from sys import (
        argv,
        exit
        )
from time import sleep

from mensa.gui import gui
from mensa.gui import read_schild_txt

if __name__ == '__main__':
    users = [user for user in read_schild_txt('Klasse052.TXT')]
    if False:
        for user in users:
            print('\n\n\n')
            print(user['name'])
            print('\n\n\n')
            add_user(user)
            sleep(2)
    gui.mainloop()

