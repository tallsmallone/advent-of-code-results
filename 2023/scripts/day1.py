import re
import unittest

import pdb

unitTesting = False

def getInput():
    f = open('../inputs/day1.txt')
    userInput = f.readlines()
    return userInput

def getCalibrationValues_part1(lines):
    total: int = 0

    for line in lines:
        if len(line) < 1:
            continue

        matches = re.findall(r'\d', line)
        firstNumber = matches[0]
        secondNumber = matches[len(matches) - 1]

        combinedNumber = firstNumber + secondNumber

        total += int(combinedNumber)
    return total

def part1():
    userInput = getInput()
    print(getCalibrationValues_part1(userInput))

def getMatches(line):
    matchesToReturn = ['', '']
    minimumIndexMatches = {}
    maximumIndexMatches = {}

    def getDigits():
        matches = re.finditer(r'\d', line)

        if matches is None:
            return

        match = next(matches, None)
        if match is None:
            return

        minimumIndexMatches['digit'] = match.start()
        matchesToReturn[0] = line[minimumIndexMatches['digit']]
        matchesToReturn[1] = line[minimumIndexMatches['digit']]

        last = next(matches, None)
        previous = minimumIndexMatches['digit']
        while last is not None:
            previous = last.start()
            last = next(matches, None)

        maximumIndexMatches['digit'] = previous

        if maximumIndexMatches['digit'] > -1:
            matchesToReturn[1] = line[maximumIndexMatches['digit']]

    def getStringMatch(number):
        matches = re.finditer(number, line)

        if matches is None:
            return

        match = next(matches, None)
        if match is None:
            return

        minimumIndexMatches[number] = match.start()

        last = next(matches, None)
        previous = minimumIndexMatches[number]
        while last is not None:
            previous = last.start()
            last = next(matches, None)

        maximumIndexMatches[number] = previous
        checkMatches(number)

    def checkMatches(number):
        skip = False

        if len(minimumIndexMatches) == 1:
            matchesToReturn[0] = number
            skip = True

        if len(maximumIndexMatches) == 1:
            matchesToReturn[1] = number
            skip = True

        if skip:
            return

        minCompare: str = matchesToReturn[0]
        maxCompare: str = matchesToReturn[1]

        if matchesToReturn[0].isdigit():
            minCompare = 'digit'

        if matchesToReturn[1].isdigit():
            maxCompare = 'digit'

        if minimumIndexMatches[number] < minimumIndexMatches[minCompare]:
            matchesToReturn[0] = number

        if maximumIndexMatches[number] > maximumIndexMatches[maxCompare]:
            matchesToReturn[1] = number

    getDigits()

    getStringMatch('zero')
    getStringMatch('one')
    getStringMatch('two')
    getStringMatch('three')
    getStringMatch('four')
    getStringMatch('five')
    getStringMatch('six')
    getStringMatch('seven')
    getStringMatch('eight')
    getStringMatch('nine')

    return matchesToReturn

def getCalibrationValues_part2(lines):
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    total: int = 0

    for line in lines:
        if len(line) < 1:
            continue

        matches = getMatches(line)

        if matches[0] == matches[1] == '':
            continue

        if matches[1] == '':
            matches[1] = matches[0]

        firstNumber = matches[0]
        secondNumber = matches[1]

        if firstNumber in numbers.keys():
            firstNumber = numbers[firstNumber]

        if secondNumber in numbers.keys():
            secondNumber = numbers[secondNumber]

        combinedNumber = firstNumber + secondNumber
        #print(combinedNumber)

        total += int(combinedNumber)
    return total

def part2():
    userInput = getInput()
    print(getCalibrationValues_part2(userInput))

class TestMatchingFunctions(unittest.TestCase):
    def test_noNumbers(self):
        self.assertEqual(0, getCalibrationValues_part2(['time']))

    def test_allNumbers(self):
        self.assertEqual(11, getCalibrationValues_part2(['11']))

    def test_allStrings(self):
        self.assertEqual(11, getCalibrationValues_part2(['oneone']))

    def test_mixed(self):
        self.assertEqual(11, getCalibrationValues_part2(['1one']))

    def test_lines(self):
        self.assertEqual(21, getCalibrationValues_part2(['11', 'onezero']))

    def test_combined(self):
        self.assertEqual(28, getCalibrationValues_part2(['2oneight']))

    def test_large(self):
        self.assertEqual(21, getCalibrationValues_part2(['2fivefncninethree3kdc1rg']))

    def test_startAndEndNumber(self):
        self.assertEqual(42, getCalibrationValues_part2(['4nineeightseven2']))

    def test_middleWordAndEndNumber(self):
        self.assertEqual(84, getCalibrationValues_part2(['cmtsnssneightthree4']))

    def test_example(self):
        self.assertEqual(281, getCalibrationValues_part2(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']))

    def test_fiveAdded(self):
        self.assertEqual(45 + 21 + 35 + 84 + 92, getCalibrationValues_part2(['four6five', '2fivefncninethree3kdc1rg', 'threef2threefivezfnnn', 'cmtsnssneightthree4', 'nine64rfnvff4krtrqskx2']))

    def test_fiveAdded2(self):
        self.assertEqual(79 + 17 + 98 + 78 + 46, getCalibrationValues_part2(['799', 'poneightnthnsmkrsixgqvmzoneninetwo7', '9seven3eight', 'seven834eightvqdrgkxnfsdqbnfgxzvg', 'qgxlnprzl4six']))

if __name__ == '__main__':
    if unitTesting:
        unittest.main()
    else:
        part2()
