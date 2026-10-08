#!/usr/bin/env python3
from services import *

class UI():
    service = Services()

    def __init__(self) -> None:
        print("--- Password Generator ---")

    def get_password(self):
        return self.service.get_last_generated_password()
