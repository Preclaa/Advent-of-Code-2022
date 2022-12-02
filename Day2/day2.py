import numpy as np
import sys

# Values for rock, paper, scissors
ROCK = 0
PAPER = 1
SCISSORS = 2

# Points for the selected shape
POINTS = {ROCK: 1,
          PAPER: 2,
          SCISSORS: 3}


def mapToRockPaperScissors(x):
    # Convert values from input to 0/1/2 (rock/paper/scissors) (or lose/draw/win for the 2nd part)
    x = x.decode()
    if x in ['A', 'X']:
        return ROCK
    if x in ['B', 'Y']:
        return PAPER
    if x in ['C', 'Z']:
        return SCISSORS
    sys.exit("Invalid input")


def rockPaperScissors(input):
    # Table with results, rows - Player1 (enemy), cols - Player2 (me)
    # Values are the end result score
    # (0 if you lost, 3 if the round was a draw, and 6 if you won)
    #               Rock    Paper   Scissors
    #   Rock         3        6         0
    #   Paper        0        3         6
    #   Scissors     6        0         3
    result = [[3, 6, 0],
              [0, 3, 6],
              [6, 0, 3]]
    # Return result of the match + score for the selected shape
    return result[input[0]][input[1]] + POINTS[input[1]]


def choosePick(input):
    # Table with enemy pick and end result, rows - Player1 (enemy), cols - Desired end result
    # Values are the shapes I need to choose
    # (0 if you lost, 3 if the round was a draw, and 6 if you won)
    #               Lose     Draw       Win
    #   Rock      Scissors   Rock      Paper
    #   Paper       Rock     Paper    Scissors
    #   Scissors   Paper    Scissors    Rock
    shape = [[SCISSORS, ROCK, PAPER],
             [ROCK, PAPER, SCISSORS],
             [PAPER, SCISSORS, ROCK]]
    # Return modified input - change 2nd col to the shape I need to pick
    return [input[0], shape[input[0]][input[1]]]


if __name__ == "__main__":
    # Load input from file, convert A/B/C/X/Y/Z to 0/1/2
    input = np.loadtxt("input.txt", dtype=int, delimiter=" ",
                       converters={
                           0: lambda x: mapToRockPaperScissors(x),
                           1: lambda x: mapToRockPaperScissors(x),
                       })
    part1 = np.sum([rockPaperScissors(item) for item in input])
    print(f"Part 1 answer: {part1}")

    # For part 2, consider values for rock(0), paper(1), scissors(2)
    # as the values for lose(0), draw(1), win(2)
    part2 = np.sum([rockPaperScissors(choosePick(item)) for item in input])
    print(f"Part 2 answer: {part2}")
