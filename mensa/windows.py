#!/usr/bin/env python3

from datetime import datetime
from random import choice
import tkinter as tk

class CardReader(tk.Frame):
    def __init__(self, master=None, gen_users=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.gen_users = gen_users
        self.key_buffer = ""

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
        self.current_name.bind("<Key>", self.print_key)
        self.current_name.focus_set()

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

    def print_key(self, event):
        if event.keycode == 36:
            print(self.key_buffer)
            tag = choice(['ok', 'rejected'])
            now = datetime.now()
            log_entry = "{}:{}\t- {}\n\n".format(now.hour, now.minute, self.key_buffer)
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert("1.0", log_entry, tag)
            self.log_text.config(state=tk.DISABLED)
            self.key_buffer = ""
        else:
            self.key_buffer += event.char
        # args = event.keysym, event.keycode, event.char
        # print("Symbol: {}, Code: {}, Char: {}".format(*args))
        # code 36 is Enter

class SetupUsers(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.current_name = tk.Label(self)
        self.current_name["text"] = "SETUP"



