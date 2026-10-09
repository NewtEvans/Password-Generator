#!/usr/bin/env python3
from ui import UI

def main():
    ui = UI()

    try:
        ui.set_password_params(ui.input_password_params())
    except ValueError as e:
        print(e)
    else:
        print(ui.get_password_params())

if __name__ == "__main__":
    main()
