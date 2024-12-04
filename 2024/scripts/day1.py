from dotenv import load_dotenv
import os
import re
import requests
import unittest
import argparse

from constants import BASE_URL, YEAR

import pdb

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

def getSumOfSmallestInLists_Part_1(lines):
    sum = 0
    left = list()
    right = list()

    for line in lines:
        a, b = line.split('   ')
        left.append(int(a))
        right.append(int(b))

    left = sorted(left)
    right = sorted(right)

    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    return sum

class TestMatchingFunctions(unittest.TestCase):
    def test_part1_oneLine(self):
        self.assertEqual(2, getSumOfSmallestInLists_Part_1(['1   3']))

    def test_part1_twoLins(self):
        self.assertEqual(4, getSumOfSmallestInLists_Part_1(['1   3', '2   4']))

    def test_part1_twoLines_unsorted(self):
        self.assertEqual(4, getSumOfSmallestInLists_Part_1(['2   4', '1   3']))

    def test_part1_example(self):
        example = [
        '3   4',
        '4   3',
        '2   5',
        '1   3',
        '3   9',
        '3   3'
        ]

        self.assertEqual(11, getSumOfSmallestInLists_Part_1(example))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code Day 1 Solution')
    parser.add_argument('-u', '--unit-test', action='store_true', help='Run unit tests')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logging')
    args = parser.parse_args()

    load_dotenv()
    
    if args.debug:
        debugging = True
    
    if args.unit_test:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        part1()