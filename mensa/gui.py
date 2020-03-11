import csv
from os.path import isfile
from random import shuffle
import tkinter as tk

from mensa.windows import (
        CardReader,
        SetupUsers
        )

def read_schild_txt(path):
    assert(isfile(path))
    try:
        with open(path) as csvfile:
            schild_reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            header = next(schild_reader)
            #if not header == ['\ufeff"Interne ID-Nummer"', 'Nachname', 'Vorname', 'Klasse']:
            #    print('Wähle das Schild Export Format:')
            #    print('Interne ID-Nummer, Nachname, Vorname, Klasse')
            #    exit(1)
            # format : ID; Nachname; Vorname; Klasse 
            users = [
                        {
                            'name': ', '.join(row[1:]),
                            'id': row[0]
                        }
                        for row in schild_reader
                    ]
            return users
    except:
        print('Schild_datei defekt ...')
        exit(1)

# Mockup / Test
def gen_users():
    users = [user for user in read_schild_txt('Klasse052.TXT')]
    shuffle(users) # works in place
    for user in users:
        yield user

root = tk.Tk()
toplevel = tk.Toplevel()
gui = CardReader(master=root, gen_users=gen_users())
setup = SetupUsers(master=toplevel)

