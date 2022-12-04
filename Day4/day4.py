import numpy as np


def convertInputToArray(input):
    # Split input (A-B) to two values, A and B
    input = [int(value) for value in input.decode().split('-')]
    # Create array {A, ..., B}
    return np.arange(input[0], input[1] + 1)


def checkSubset(input):
    # Calculate union of two arrays
    # If the union size is the same as one of the input arrays, then it is a subset
    return np.union1d(input[0], input[1]).size in [input[0].size, input[1].size]


def checkIntersection(input):
    # Calculate intersecstion of two arrays
    # If the intersection size is greater than 0, then arrays intersect
    return np.intersect1d(input[0], input[1]).size > 0


if __name__ == "__main__":
    # Load input from file, split row to two columns
    # and create numpy array for each col
    input = np.loadtxt("input.txt", dtype=list, delimiter=",",
                       converters=convertInputToArray)

    part1 = np.sum([checkSubset(line) for line in input])
    print(f"Part 1 answer: {part1}")

    part2 = np.sum([checkIntersection(line) for line in input])
    print(f"Part 2 answer: {part2}")
