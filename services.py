#!/usr/bin/env python3
import random

class Services:
    def __init__(self) -> None:

        self._password_parameters = {
            "password_length": 0,
            "includes_uppercases": False,
            "includes_lowercase": False,
            "includes_numbers": False,
            "includes_symbols": False,
         }

        self._last_generated_password = ""

    def input_password_params(self, password_length: int, includes_uppercases: bool, includes_lowercases: bool,  includes_numbers: bool, includes_symbols: bool) -> dict:

        dict = {
            "password_length": password_length,
            "includes_uppercases": includes_uppercases,
            "includes_lowercases": includes_lowercases,
            "includes_numbers": includes_numbers,
            "includes_symbols": includes_symbols,
        }

        return dict

    @property
    def password_parameters(self) -> dict:
        return dict(self._password_parameters)

    @password_parameters.setter
    def password_parameters(self, requested_options: dict) -> None:
        #TODO need to be fixed
        if not self._password_parameters.keys() == requested_options.keys():
            raise Exception("dict needs to contain all keys")
        if self._password_parameters["includes_uppercases"] == False and self._password_parameters["includes_lowercases"] == False:
            raise Exeption("at least one type of cases has to be true")
        self._password_parameters = self._password_parameters | requested_options

    def generate_password(self) -> None:
        from random import randint
        password_length = self._password_parameters["password_length"]
        #TODO needs to find out, how ti mix uppercases and lowercases - mby I can separete the uppercases and lower cases
        usable_symbols = ""
        password = ""

        if self._password_parameters["includes_uppercases"] == True:
            usable_symbols += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self._password_parameters["includes_lowercases"] == True:
            usable_symbols += "abcdefghijklmnopqrstuvwxyz"
        if self._password_parameters["includes_numbers"] == True:
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
