#!/usr/bin/env python3
import random

class Services:
    def __init__(self) -> None:

        self._password_parameters = {
            "password_length": 0,
            "includes_numbers": False,
            "includes_symbols": False,
         }

        self._last_generated_password = ""

    def input_password_params(self, password_length: int, includes_numbers: bool, includes_symbols: bool) -> dict:

        dict = {
            "password_length": password_length,
            "includes_numbers": includes_numbers,
            "includes_symbols": includes_symbols,
        }

        return dict

    @property
    def password_parameters(self) -> dict:
        return dict(self._password_parameters)

    @password_parameters.setter
    def password_parameters(self, requested_options: dict) -> None:
        if not self._password_parameters.keys() == requested_options.keys():
            raise Exception("dict needs to contain all keys")
        self._password_parameters = self._password_parameters | requested_options

    def generate_password(self) -> None:
        from random import randint
        password_length = self._password_parameters["password_length"]
        usable_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = ""


        if self._password_parameters["includes_number"] == True:
            usable_symbols += "123456789"
        if self._password_parameters["includes_symbols"] == True:
            usable_symbols += "!@#$%^&*"

        for _ in range(password_length):
            password += usable_symbols[randint(0, len(usable_symbols) - 1)]
            self._last_generated_password = password

    @property
    def last_generated_password(self):
        return self._last_generated_password

    # helper functions
    def _random_number(self) -> int:
        number = random.randint(1, 5)

        return number
