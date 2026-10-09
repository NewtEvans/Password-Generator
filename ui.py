#!/usr/bin/env python3
from services import *

class UI:
    service = Services()

    def __init__(self) -> None:
        print("--- Password Generator ---")

    def input_password_params(self) -> dict:
        password_length = int(input("insert password_length: "))
        includes_numbers = bool(input("numbers? True/False: "))
        includes_symbols = bool(input("symbols? True/False: "))

        return self.service.input_password_params(password_length, includes_numbers, includes_symbols)

    def set_password_params(self, requested_params: dict) -> None:
        self.service.password_parameters = requested_params

    def get_password_params(self):
        return self.service.password_parameters
