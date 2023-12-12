from dotenv import load_dotenv
import os
import re
import requests
import unittest

from constants import BASE_URL, YEAR

import pdb

unitTesting = False
debugging = True

def getInput():
    headers = {'Cookie': f"session={os.getenv('AOC_SESSION')}"}
    input = requests.get(f'{BASE_URL}/{YEAR}/day/3/input', headers=headers)
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
    print(f'{len(userInput)}')
    print(getSumOfPartNumbers_part1(userInput))

def getSumOfPartNumbers_part1(lines):
    numbersRegex = r'\d+'
    symbolsRegex = r'[^.\d]'

    validNumberIndexes = set()
    totalPartNumber = 0

    for index, line in enumerate(lines):
        for matchFound in re.finditer(symbolsRegex, line):
            matchStart = matchFound.start()
            validNumberIndexes |= {(row, column)
                                   for row in range(index - 1, index + 2)
                                   for column in range(matchStart - 1, matchStart + 2)}

    for index, line in enumerate(lines):
        for matchFound in re.finditer(numbersRegex, line):
            if any((index, column) in validNumberIndexes for column in range(*matchFound.span())):
                totalPartNumber += int(matchFound.group())

    return totalPartNumber

class TestMatchingFunctions(unittest.TestCase):
    def test_part1_oneLine(self):
        self.assertEqual(1, getSumOfPartNumbers_part1(['.......#1.']))

    def test_part1_oneLine_doubleDigits(self):
        self.assertEqual(10, getSumOfPartNumbers_part1(['.......#10.']))

    def test_part1_oneLine_twoNumbers(self):
        self.assertEqual(15, getSumOfPartNumbers_part1(['...%5....#10.']))

    def test_part1_oneLine_doubleDigits_twoNumbers(self):
        self.assertEqual(30, getSumOfPartNumbers_part1(['..@20.....#10.']))

    def test_part1_oneLine_tripleDigits_twoNumbers(self):
        self.assertEqual(320, getSumOfPartNumbers_part1(['..@200.....#120.']))

    def test_part1_noNumbers(self):
        self.assertEqual(0, getSumOfPartNumbers_part1(['.......#..']))

    def test_part1_twoLines(self):
        self.assertEqual(1, getSumOfPartNumbers_part1(['.......#..',
                                                       '........1.']))

    def test_part1_twoLines_noNumbers(self):
        self.assertEqual(0, getSumOfPartNumbers_part1(['.......#..',
                                                       '..........']))

    def test_part1_twoLines_doubleDigits(self):
        self.assertEqual(10, getSumOfPartNumbers_part1(['.......#..',
                                                       '........10.']))

    def test_part1_threeLines_doubleDigits(self):
        self.assertEqual(10, getSumOfPartNumbers_part1(['.......#..',
                                                       '........10.',
                                                       '..........']))

    def test_part1_threeLines_duplicates(self):
        self.assertEqual(10, getSumOfPartNumbers_part1(['.......#..',
                                                       '........10.',
                                                       '........@.']))

    def test_part1_example(self):
        self.assertEqual(4361, getSumOfPartNumbers_part1(['467..114..',
                                                          '...*......',
                                                          '..35..633.',
                                                          '......#...',
                                                          '617*......',
                                                          '.....+.58.',
                                                          '..592.....',
                                                          '......755.',
                                                          '...$.*....',
                                                          '..664.598..']))

    def test_part1_longLine(self):
        self.assertEqual(0, getSumOfPartNumbers_part1(['............409..........784...578...802......64..............................486.248..............177....................369...............']))

    def test_part1_twoLongLine(self):
        self.assertEqual(4173, getSumOfPartNumbers_part1(['............409..........784...578...802......64..............................486.248..............177....................369...............',
                                                          '.....-939..........524#...#....=.......*.........+......90.................................76..615..-..@.....961..........$.......*.........']))

if __name__ == '__main__':
    load_dotenv()

    if unitTesting:
        unittest.main()
    else:
        part1()