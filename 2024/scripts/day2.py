"""
Day 2 solution for Advent of Code.
This module handles processing and comparing lists of numbers.
"""

import unittest
import argparse

from utilities import get_input, log

DEBUGGING = True

DELIMITER = ' '
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 3

def part1():
    """Run the solution for part 1 of the puzzle."""
    print(get_number_of_safe_reports(get_input(2)))

def part2():
    """Run the solution for part 2 of the puzzle."""
    pass


def get_number_of_safe_reports(lines: list):
    """
    Calculate the number of "safe" reports.

    A report is considered safe if the difference between the current and last levels
    is between MIN_DIFFERENCE and MAX_DIFFERENCE.

    Args:
        lines (list): List of strings, each containing a number that represents a level.

    Returns:
        int: The number of safe reports.
    """

    def is_valid_increasing_report(current_level: int, last_level: int) -> bool:
        if current_level < last_level:
            return False

        difference = current_level - last_level
        return (difference >= MIN_DIFFERENCE and difference <= MAX_DIFFERENCE)

    def is_valid_decreasing_report(current_level: int, last_level: int) -> bool:
        if current_level > last_level:
            return False

        difference = last_level - current_level
        return (difference >= MIN_DIFFERENCE and difference <= MAX_DIFFERENCE)

    total = 0

    for line in lines:
        levels = line.split(DELIMITER)

        good_line = True
        direction = 0

        for index, level in enumerate(levels):
            if index == 0 or not good_line:
                continue

            current_level = int(level)
            last_level = int(levels[index - 1])

            if is_valid_increasing_report(current_level, last_level) \
                and (direction == 0 or direction == 1):
                direction = 1
            elif is_valid_decreasing_report(current_level, last_level) \
                and (direction == 0 or direction == -1):
                direction = -1
            else:
                good_line = False

        if good_line:
            log('good line', line)
            total += 1

    return total


class TestMatchingFunctions(unittest.TestCase):
    """Test cases for the matching functions in Day 2 solution."""

    # def test_part_1_one_line(self):
    #     """Test part 1 with a single line input."""
    #     self.assertEqual(1, get_number_of_safe_reports(['1 2 3 4 5']))

    # def test_part_1_two_lines(self):
    #     """Test part 1 with two lines input."""
    #     self.assertEqual(2, get_number_of_safe_reports(['1 2 3 4 5', '2 3 4 5 6']))

    # def test_part_1_one_line_unsafe(self):
    #     """Test part 1 with a single unsafe line input."""
    #     self.assertEqual(0, get_number_of_safe_reports(['1 2 3 1 5']))

    # def test_part_1_two_lines_unsafe(self):
    #     """Test part 1 with two unsafe lines input."""
    #     self.assertEqual(0, get_number_of_safe_reports(['1 2 3 1 5', '2 3 4 1 6']))

    def test_part_1_example(self):
        """Test part 1 with the complete example input set from the problem."""
        example = [
            '7 6 4 2 1',
            '1 2 7 8 9',
            '9 7 6 2 1',
            '1 3 2 4 5',
            '8 6 4 4 1',
            '1 3 6 7 9',
        ]

        self.assertEqual(2, get_number_of_safe_reports(example))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code Day 2 Solution')
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
