#!/usr/bin/env python3
from services import Services

def main():
    services = Services()

    for _ in range(5):
        print(services.random_number())

if __name__ == "__main__":
    main()
