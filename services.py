#!/usr/bin/env python3
import random

class Services:
    _LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _NUMBERS = "123456789"
    _SYMBOLS = "!@#$%^&*()-+=/~|"

    def __init__(self) -> None:

        self._password_parameters = {
            "password_length": 0,
            "includes_numbers": False,
            "includes_symbols": False,
         }

        self._last_generated_password = ""

    @property
    def password_parameters(self) -> dict:
        return dict(self._password_parameters)

    @password_parameters.setter
    def password_parameters(self, requested_options: dict) -> None:
        if not self._password_parameters.keys() == requested_options.keys():
            raise Exception("dict needs to contain all keys")
        self._password_parameters = self._password_parameters | requested_options


    

    def _generate_password(self, ):
        pass


    def set_password(self, password_parameters: dict):
        pass

    @property
    def get_last_generated_password(self):
        return self._last_generated_password

    # helper functions
    def _random_number(self) -> int:
        number = random.randint(1, 5)

        return number
