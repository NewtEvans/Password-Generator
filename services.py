#!/usr/bin/env python3
import random

class Services():

    __LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __NUMBERS = "123456789"
    __SYMBOLS = "!@#$%^&*()-+=/~|"

    __available_password_symbols = ""

    _last_generated_password = "hovno"

    def get_password_parameters(self, options: dict) -> str:

        return ""

    def _generate_password(self, ):
        pass


    def get_last_generated_password(self):
        return self._last_generated_password

    # helper functions
    def _random_number(self) -> int:
        number = random.randint(1, 5)

        return number
