import unittest
import argparse

import pdb

from utilities import getInput, log

debugging = True

DELIMITER = '   '

def part1():
    userInput = getInput()
    print(getSumOfSmallestInLists_Part_1(userInput))

def part2():
    userInput = getInput()
    print(getSimilarityScore_Part_2(userInput))

def getSumOfSmallestInLists_Part_1(lines):
    sum = 0
    left = list()
    right = list()

    for line in lines:
        a, b = line.split(DELIMITER)
        left.append(int(a))
        right.append(int(b))

    left = sorted(left)
    right = sorted(right)

    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    return sum

def getSimilarityScore_Part_2(lines):
    total = 0
    left = list()
    right = list()

    amount = dict()

    for line in lines:
        a, b = line.split(DELIMITER)
        left.append(int(a))
        right.append(int(b))

    left = sorted(left)
    right = sorted(right)

    for i in range(len(left)):
        if left[i] not in amount:
            temp_total = 0
            for j in range(len(right)):
                if left[i] == right[j]:
                    temp_total += right[j]
            amount[left[i]] = temp_total

        total += amount[left[i]]

    return total

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

    def test_part2_oneLine(self):
        self.assertEqual(0, getSimilarityScore_Part_2(['1   3']))

    def test_part2_oneLine_match(self):
        self.assertEqual(1, getSimilarityScore_Part_2(['1   1']))

    def test_part2_twoLines(self):
        self.assertEqual(0, getSimilarityScore_Part_2(['1   3', '2   4']))

    def test_part2_twoLines_match(self):
        self.assertEqual(3, getSimilarityScore_Part_2(['1   1', '2   2']))

    def test_part2_example(self):
        example = [
        '3   4',
        '4   3',
        '2   5',
        '1   3',
        '3   9',
        '3   3'
        ]

        self.assertEqual(31, getSimilarityScore_Part_2(example))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code Day 1 Solution')
    parser.add_argument('-u', '--unit-test', action='store_true', help='Run unit tests')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('-2', '--part-2', action='store_true', help='Run part 2 solution')
    args = parser.parse_args()

    if args.debug:
        debugging = True

    if args.unit_test:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        if args.part_2:
            part2()
        else:
            part1()