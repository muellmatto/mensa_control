#!/usr/bin/env python3

import csv
from datetime import datetime
from os.path import isfile
from random import choice, shuffle
from time import sleep
import tkinter as tk
from sys import (
        argv,
        exit
        )


# MA300
from zk import const, ZK
# zk == pyzk

zk = ZK(
        ip='192.168.1.201',
        port=4370,
        timeout=20,
        password=0,
        force_udp=True,
        ommit_ping=False
        )


# GUI
class Application(tk.Frame):
    def __init__(self, master=None, gen_users=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.gen_users = gen_users

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\nClick me"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.current_name = tk.Label(self)
        self.current_name["bd"] = 2
        self.current_name["bg"] = 'green'
        self.current_name.config(
                font=("Noto", 16),
                width=50,
                height=1
                )
        self.current_name["text"] = "... ready ..."
        self.current_name.pack(side="top")

        self.log_text = tk.Text(self)
        self.log_text.config(
                state=tk.DISABLED,
                width=120,
                height=30
                )
        self.log_text.tag_config('ok', background='green')
        self.log_text.tag_config('rejected', background='red')
        self.log_text.pack()

    def say_hi(self):
        print("hi there, everyone")
        self.hi_there["text"] += '!'
        tag = choice(['ok', 'rejected'])
        user = next(self.gen_users)
        name = user['name']
        now = datetime.now()
        log_entry = "{}:{}\t- {}\n\n".format(now.hour, now.minute, name)
        if tag == "ok":
            self.current_name["bg"] = "green"
            self.current_name["text"] = name
        else:
            self.current_name["bg"] = "red"
            self.current_name["text"] = name

        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert("1.0", log_entry, tag)
        # self.log_text.insert(tk.END, log_entry, tag)
        self.log_text.config(state=tk.DISABLED)


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

def get_device_users():
    conn = zk.connect()
    users = conn.get_users()
    print(users)


def add_user(user):
    conn = zk.connect()
    conn.set_user(
            uid=int(user['id']),
            name=user['name'],
            privilege=const.USER_DEFAULT,
            user_id=str(user['id'])
            )
    zk.enroll_user(user_id=str(user['id']))

def gen_users():
    users = [user for user in read_schild_txt('Klasse052.TXT')]
    shuffle(users) # works in place
    for user in users:
        yield user


if __name__ == '__main__':
    users = [user for user in read_schild_txt('Klasse052.TXT')]
    if False:
        for user in users:
            print('\n\n\n')
            print(user['name'])
            print('\n\n\n')
            add_user(user)
            sleep(2)

    root = tk.Tk()
    app = Application(master=root, gen_users=gen_users())
    app.mainloop()
