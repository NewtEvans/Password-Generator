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
    service = Services()

    password_length = 8
    includes_uppercases = False
    includes_lowercases = True
    includes_numbers = False
    includes_symbols = False

    def password_generation_handler(self):
        self.service.password_parameters = self.service.input_password_params(self.password_length, self.u_case_var.get(), self.l_case_var.get(), self.numbers_var.get(), self.symbols_var.get())
        self.service.generate_password()
        self.password_label.config(text = self.service.last_generated_password)

    def __init__(self):
        self.service.password_parameters = self.service.input_password_params(self.password_length, self.includes_uppercases, self.includes_lowercases, self.includes_numbers, self.includes_symbols)
        print(self.service.password_parameters)
        #root window
        #window title
        #window resolutions
        root = Tk()
        root.title("Password Generator")
        root.geometry("500x100")

        #adding a label to the root
        label = Label(root, text="Length")
        label.grid()

        #adding an entry field
        length_field = Entry(root, width=2)
        length_field.grid(column=1, row=0)
        #all widgets will be here
        #has to be the last function

        self.u_case_var = BooleanVar()
        self.l_case_var = BooleanVar()
        self.numbers_var = BooleanVar()
        self.symbols_var = BooleanVar()

        #options
        #TODO mayby group them somehow
        self.upper_cases = Checkbutton(root, text="Enable uppercases", variable=self.u_case_var)
        self.upper_cases.grid(row=2, column=1)
        self.lower_cases = Checkbutton(root, text="Enable lowercases", variable=self.l_case_var)
        self.lower_cases.grid(row=2, column=0)
        self.numbers = Checkbutton(root, text="Enable numbers", variable=self.numbers_var)
        self.numbers.grid(row=2, column=2)
        self.symbols = Checkbutton(root, text="Enable symbols", variable=self.symbols_var)
        self.symbols.grid(row=2, column=3)

        button = Button(root, text="Generate", command=self.password_generation_handler)
        button.grid(row=3, column=0)

        self.password_label = Label(root)
        self.password_label.grid(row=4, column=0)

        #windows resize disable
       # root.resizable(False, False)
        #mainloop
        root.mainloop()
