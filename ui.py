#!/usr/bin/env python3
from services import *
from tkinter import *


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

    password_length = 0
    includes_uppercases = False
    includes_lowercases = True
    includes_numbers = False
    includes_symbols = False

    def password_generation_handler(self):
        try:
            self.service.password_parameters = self.service.input_password_params(self.length_var.get(), self.u_case_var.get(), self.l_case_var.get(), self.numbers_var.get(), self.symbols_var.get())
        except Exception as e:
            self._return_text_into_label(e)
        else:
            self.service.generate_password()
            self._return_text_into_label()


    def copy_button_handler(self):
        self.root.clipboard_clear()
        #TODO this needs to be updated - it's possible to copy error message now
        if self.service.last_generated_password== "":
            raise Exception("password is not generated yet")
        if self.last_message != self.service.last_generated_password:
            raise Exception("generate valid password first")
        self.root.clipboard_append(self.service.last_generated_password)
        self.message_label.config(text = f"Copied!")
        self.root.after(800, self._return_text_into_label)

    def __init__(self):
        self.service.password_parameters = self.service.input_password_params(self.password_length, self.includes_uppercases, self.includes_lowercases, self.includes_numbers, self.includes_symbols)
        print(self.service.password_parameters)
        #root window
        #window title
        #window resolutions
        self.root = Tk()
        self.root.title("Password Generator")
        self.root.geometry("500x100")

        #adding a label to the root
        label = Label(self.root, text="Length")
        label.grid(row=0, column=0)

        self.length_var = IntVar(value=6)

        #adding an entry field
        length_field = Entry(self.root, width=2, textvariable=self.length_var)
        length_field.grid(row=0, column=1)
        #all widgets will be here
        #has to be the last function

        self.u_case_var = BooleanVar()
        self.l_case_var = BooleanVar()
        self.numbers_var = BooleanVar()
        self.symbols_var = BooleanVar()

        #options
        #TODO mayby group them somehow
        self.upper_cases = Checkbutton(self.root, text="Enable uppercases", variable=self.u_case_var)
        self.upper_cases.grid(row=2, column=1)
        self.lower_cases = Checkbutton(self.root, text="Enable lowercases", variable=self.l_case_var)
        self.lower_cases.grid(row=2, column=0)
        self.numbers = Checkbutton(self.root, text="Enable numbers", variable=self.numbers_var)
        self.numbers.grid(row=2, column=2)
        self.symbols = Checkbutton(self.root, text="Enable symbols", variable=self.symbols_var)
        self.symbols.grid(row=2, column=3)

        button_generate = Button(self.root, text="Generate", command=self.password_generation_handler)
        button_generate.grid(row=3, column=0)
        button_copy = Button(self.root, text="Copy", command=self.copy_button_handler)
        button_copy.grid(row=3, column=3)


        #TODO I want to change password label into message label and print there also error messages
        self.message_label = Label(self.root)
        self.message_label.grid(row=4, columnspan=3)

        #windows resize disable
        self.root.resizable(False, False)
        #mainloop
        self.root.mainloop()

   # def _return_password_into_label(self) -> None:
   #     self.message_label.config(text = self.service.last_generated_password)
    last_message = ""

    def _return_text_into_label(self, message=None) -> None:
        if isinstance(message, Exception):
            self.last_message = str(message)
            self.message_label.config(text = self.last_message, foreground="red")
        else:
            self.last_message = self.service.last_generated_password
            self.message_label.config(text = self.last_message, foreground="green")
