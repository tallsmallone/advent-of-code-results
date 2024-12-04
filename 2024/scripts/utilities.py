"""
Utility functions for Advent of Code solutions.

This module provides common functionality used across different Advent of Code solutions,
including input retrieval and debug logging capabilities.

Functions:
    getInput(): Retrieves the input for the current day's puzzle using session credentials
    log(name, value, debugging): Prints debug information when debugging is enabled
"""

import os
from dotenv import load_dotenv
import requests

from constants import BASE_URL, YEAR

def get_input(day: int):
    """
    Retrieves the input for the current day's puzzle using session credentials.

    The environment variable AOC_SESSION must be set to a valid session cookie
    from the Advent of Code website.

    Returns:
        A list of strings where each string is a line of the input.
    """
    load_dotenv()

    headers = {'Cookie': f"session={os.getenv('AOC_SESSION')}"}
    result = requests.get(f'{BASE_URL}/{YEAR}/day/{day}/input', headers=headers, timeout=10)
    body = result.content.decode().splitlines()
    return body

def log(name, value = None, debugging = True):
    """
    Prints debug information when debugging is enabled.

    If the optional value parameter is provided, it is printed after the name.
    If the optional debugging parameter is False, the function does nothing.

    Parameters:
        name (str): The name to be printed
        value (any): The value to be printed after the name
        debugging (bool): Whether to print anything
    """
    if debugging:
        if value is not None:
            print(f'{name}: [{value}]')
        else:
            print(f'{name}')
