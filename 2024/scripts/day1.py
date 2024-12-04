from dotenv import load_dotenv
import os
import re
import requests
import unittest

from constants import BASE_URL, YEAR

import pdb

unitTesting = True
debugging = True

def getInput():
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

def part1():
    userInput = getInput()
    print(getSumOfSmallestInLists_Part_1(userInput))

class TestMatchingFunctions(unittest.TestCase):
    def test_part1_oneLine(self):
        self.assertEqual(2, getSumOfSmallestInLists_Part_1(['1    3']))

if __name__ == '__main__':
    load_dotenv()

    if unitTesting:
        unittest.main()
    else:
        part1()