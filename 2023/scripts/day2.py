import unittest

import pdb

unitTesting = False

def getInput():
    f = open('../inputs/day2.txt')
    userInput = f.readlines()
    return userInput

def part1():
    userInput = getInput()
    print(getPossibleGames_part1(userInput))

def getPossibleGames_part1(lines):
    maxBalls = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    totalPossibleGames = 0

    for line in lines:
        information = line.split(':')
        gameTitle = information[0]
        game = gameTitle.split(' ')[1]
        results = information[1]
        sets = results.split(';')

        possible = True
        for singleSet in sets:
            balls = singleSet.split(',')
            for ball in balls:
                singleBallColor = ball.strip().split(' ')
                number = singleBallColor[0]
                color = singleBallColor[1]

                if int(number) > maxBalls[color]:
                    possible = False
                    break

            if not possible: break

        if possible:
            totalPossibleGames += int(game)

    return totalPossibleGames

def part2():
    userInput = getInput()
    print(getPossibleGames_part2(userInput))

def getPossibleGames_part2(lines):
    totalPowers = 0

    for line in lines:
        minimumBalls = {
            'red': 0,
            'blue': 0,
            'green': 0
        }

        information = line.split(':')
        results = information[1]
        sets = results.split(';')

        for singleSet in sets:
            balls = singleSet.split(',')
            for ball in balls:
                singleBallColor = ball.strip().split(' ')
                number = singleBallColor[0]
                color = singleBallColor[1]

                if int(number) > minimumBalls[color]:
                    minimumBalls[color] = int(number)

        amountToAdd = minimumBalls['red'] * minimumBalls['blue'] * minimumBalls['green']

        totalPowers += amountToAdd

    return totalPowers

class TestMatchingFunctions(unittest.TestCase):
    def test_part1_1game(self):
        self.assertEqual(1, getPossibleGames_part1(['Game 1: 4 red, 3 blue']))

    def test_part1_1game_multipleSets(self):
        self.assertEqual(1, getPossibleGames_part1(['Game 1: 4 red, 3 blue 6 blue, 10 green; 9 blue, 13 green, 1 red; 10 green, 4 red, 6 blue']))

    def test_part1_1game_multipleSets_impossible(self):
        self.assertEqual(0, getPossibleGames_part1(['Game 1: 4 red, 3 blue 6 blue, 10 green; 9 blue, 16 green, 1 red; 10 green, 4 red, 6 blue']))

    def test_part1_2games_multipleSets(self):
        self.assertEqual(2, getPossibleGames_part1(['Game 1: 4 red, 3 blue; 6 blue, 16 green; 9 blue, 13 green, 1 red; 10 green, 4 red, 6 blue',
                                                    'Game 2: 2 green, 3 blue; 11 red; 2 green, 5 red, 1 blue']))

    def test_part1_example(self):
        self.assertEqual(8, getPossibleGames_part1(['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                                                    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                                                    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                                                    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                                                    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']))

    def test_part2_1game_zero(self):
        self.assertEqual(0, getPossibleGames_part2(['Game 1: 4 red, 3 blue']))

    def test_part2_1game(self):
        self.assertEqual(12, getPossibleGames_part2(['Game 1: 4 red, 3 blue, 1 green']))

    def test_part2_example(self):
        self.assertEqual(2286, getPossibleGames_part2(['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                                                    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                                                    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                                                    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                                                    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']))

if __name__ == '__main__':
    if unitTesting:
        unittest.main()
    else:
        part2()