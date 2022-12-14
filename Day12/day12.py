import numpy as np


def getElevation(item):
    return ord(item) - ord('a')


def splitRowToColumns(row):
    # Splits input string to list and converts items to int
    return [getElevation(item) for item in row.decode()]


if __name__ == "__main__":
    # Load input from file
    input = np.loadtxt("input.txt", dtype=list, converters=splitRowToColumns)
    # Convert input to numpy matrix
    matrix = np.array([row for row in input])

    # Get index of starting and ending position
    start = [np.where(matrix == getElevation('S'))[0][0],
             np.where(matrix == getElevation('S'))[1][0]]
    end = [np.where(matrix == getElevation('E'))[0][0],
           np.where(matrix == getElevation('E'))[1][0]]
    # Replace starting and ending position with given elevation
    matrix[matrix == getElevation('S')] = getElevation('a')
    matrix[matrix == getElevation('E')] = getElevation('z')

    print(start, end)
    print(matrix)
