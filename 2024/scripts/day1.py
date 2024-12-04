"""
Day 1 solution for Advent of Code.
This module handles processing and comparing lists of numbers.
"""

import unittest
import argparse

from utilities import get_input

DEBUGGING = True

DELIMITER = '   '

def part1():
    """Run the solution for part 1 of the puzzle."""
    print(get_sum_of_smallest_in_lists_part_1(get_input()))

def part2():
    """Run the solution for part 2 of the puzzle."""
    print(get_similarity_score_part_2(get_input()))

def get_sum_of_smallest_in_lists_part_1(lines):
    """
    Calculate the sum of absolute differences between sorted pairs of numbers.

    Args:
        lines (list): List of strings, each containing two numbers separated by DELIMITER

    Returns:
        int: Sum of absolute differences between corresponding sorted numbers
    """
    total = 0
    left = list()
    right = list()

    for line in lines:
        a, b = line.split(DELIMITER)
        left.append(int(a))
        right.append(int(b))

    left = sorted(left)
    right = sorted(right)

    for i, left_val in enumerate(left):
        total += abs(left_val - right[i])

    return total

def get_similarity_score_part_2(lines):
    """
    Calculate similarity score by summing matching numbers in sorted pairs.

    Args:
        lines (list): List of strings, each containing two numbers separated by DELIMITER

    Returns:
        int: Total similarity score based on matching numbers
    """
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

    for _, left_val in enumerate(left):
        if left_val not in amount:
            temp_total = 0
            for _, right_val in enumerate(right):
                if left_val == right_val:
                    temp_total += right_val
            amount[left_val] = temp_total

        total += amount[left_val]

    return total

class TestMatchingFunctions(unittest.TestCase):
    """Test cases for the matching functions in Day 1 solution."""

    def test_part_1_one_line(self):
        """Test part 1 with a single line input."""
        self.assertEqual(2, get_sum_of_smallest_in_lists_part_1(['1   3']))

    def test_part_1_two_lines(self):
        """Test part 1 with two lines input."""
        self.assertEqual(4, get_sum_of_smallest_in_lists_part_1(['1   3', '2   4']))

    def test_part_1_two_lines_unsorted(self):
        """Test part 1 with two unsorted lines input."""
        self.assertEqual(4, get_sum_of_smallest_in_lists_part_1(['2   4', '1   3']))

    def test_part_1_example(self):
        """Test part 1 with the complete example input set from the problem."""
        example = [
        '3   4',
        '4   3',
        '2   5',
        '1   3',
        '3   9',
        '3   3'
        ]

        self.assertEqual(11, get_sum_of_smallest_in_lists_part_1(example))

    def test_part_2_one_line(self):
        """Test part 2 with a single line input."""
        self.assertEqual(0, get_similarity_score_part_2(['1   3']))

    def test_part_2_one_line_match(self):
        """Test part 2 with a single line matching input."""
        self.assertEqual(1, get_similarity_score_part_2(['1   1']))

    def test_part_2_two_lines(self):
        """Test part 2 with two lines input."""
        self.assertEqual(0, get_similarity_score_part_2(['1   3', '2   4']))

    def test_part_2_two_lines_match(self):
        """Test part 2 with two lines matching input."""
        self.assertEqual(3, get_similarity_score_part_2(['1   1', '2   2']))

    def test_part_2_example(self):
        """Test part 2 with the complete example input set from the problem."""
        example = [
        '3   4',
        '4   3',
        '2   5',
        '1   3',
        '3   9',
        '3   3'
        ]

        self.assertEqual(31, get_similarity_score_part_2(example))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code Day 1 Solution')
    parser.add_argument('-u', '--unit-test', action='store_true', help='Run unit tests')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('-2', '--part-2', action='store_true', help='Run part 2 solution')
    args = parser.parse_args()

    if args.debug:
        DEBUGGING = True

    if args.unit_test:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        if args.part_2:
            part2()
        else:
            part1()
