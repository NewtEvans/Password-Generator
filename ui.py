#!/usr/bin/env python3
from services import *
from tkinter import *
from tkinter import ttk

class TerminalUI:
    service = Services()

    def __init__(self) -> None:
        print("--- Password Generator ---")

    def input_password_params(self) -> dict:
        password_length = int(input("insert password_length: "))
        includes_uppercases = bool(input("uppercases? True/False: "))
        includes_lowercases = bool(input("lowercases? True/False: "))
        includes_numbers = bool(input("numbers? True/False: "))
        includes_symbols = bool(input("symbols? True/False: "))

        return self.service.input_password_params(password_length, includes_uppercases, includes_lowercases, includes_numbers, includes_symbols)

    def set_password_params(self, requested_params: dict) -> None:
        self.service.password_parameters = requested_params

    def get_password_params(self):
        return self.service.password_parameters

    def set_password(self):
        self.service.generate_password()

    def get_password(self):
        return self.service.last_generated_password

class WindowUI:
    #root window
    #window title
    #window resolutions
    root = Tk()
    root.title("Password Generator")
    root.geometry("250x150")

    #adding a label to the root
    label = Label(root, text="Length")
    label.grid()

    #adding an entry field
    length_field = Entry(root, width=2)
    length_field.grid(column=1, row=0)
    #all widgets will be here
    #has to be the last function
    root.mainloop()
