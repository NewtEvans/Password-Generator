#!/usr/bin/env python3
from services import *
import pytest

def test_password_parameters_dictionary():
    service = Services()
    password_parameters = {
            "password_length": 4,
            "includes_uppercases": True,
            "includes_lowercases": False,
            "includes_numbers": False,
            "includes_symbols": False,
         }

    service.password_parameters = password_parameters

    assert service.password_parameters == password_parameters

def test_lower_and_upper_cases_false():
    service = Services()
    password_parameters = {
            "password_length": 6,
            "includes_uppercases": False,
            "includes_lowercases": False,
            "includes_numbers": True,
            "includes_symbols": False,
         }

    with pytest.raises(Exception, match="at least one type of cases has to be true"):
        service.password_parameters = password_parameters
