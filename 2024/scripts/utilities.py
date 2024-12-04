from dotenv import load_dotenv
import os
import requests

from constants import BASE_URL, YEAR

def getInput():
    load_dotenv()

    headers = {'Cookie': f"session={os.getenv('AOC_SESSION')}"}
    input = requests.get(f'{BASE_URL}/{YEAR}/day/1/input', headers=headers)
    userInput = input.content.decode().splitlines()
    return userInput

def log(name, value = None):
    if debugging:
        if value is not None:
            print(f'{name}: [{value}]')
        else:
            print(f'{name}')