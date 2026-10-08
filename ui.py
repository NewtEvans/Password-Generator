#!/usr/bin/env python3
from services import *

class UI:
    service = Services()

    def __init__(self) -> None:
        print("--- Password Generator ---")

    def set_password_params(self, requested_params: dict) -> None:
        self.service.password_parameters = requested_params

    def get_password_params(self):
        return self.service.password_parameters
