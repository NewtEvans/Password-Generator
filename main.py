#!/usr/bin/env python3
from ui import UI

def main():
    d1 = {
        "password_length": 4,
        "includes_numbers": False,
        "includes_symbols": True,
        }
    d2 = {
        "password_length": 8,
        "includes_numbers": True,
        "includes_symbols": False,
        }
    dr = {
        'hovno': "ano",
        "includes_numbers": True
    }

    ui = UI()

    ui.set_password_params(d1)
    print(ui.get_password_params())

    ui.set_password_params(d2)
    print(ui.get_password_params())

    ui.set_password_params(dr)

    ui.set_password_params(d1)
    print(ui.get_password_params())


if __name__ == "__main__":
    main()
