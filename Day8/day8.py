import numpy as np


def splitRowToColumns(row):
    # Splits input string to list and converts items to int
    return [int(item) for item in row.decode()]


def calculateVisibleTrees(currentTree, trees):
    # Calculates number of visible trees
    visibleTrees = 0
    for tree in trees:
        visibleTrees += 1
        if tree >= currentTree:
            return visibleTrees
    return visibleTrees


if __name__ == "__main__":
    # Load input from file
    input = np.loadtxt("input.txt", dtype=list, converters=splitRowToColumns)
    # Convert input to numpy matrix
    matrix = np.array([row for row in input])

    treesVisible = 0
    scenicScores = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            currentTree = matrix[i][j]
            # Get list of trees on each side of the current tree
            trees = [
                matrix[i][0:j][::-1],   # Left
                matrix[i][j + 1 :],     # Right
                matrix.T[j][0:i][::-1], # Up
                matrix.T[j][i + 1 :],   # Down
            ]
            # Calculate the max height of trees on each side
            maxHeight = [np.max(tree, initial=-1) for tree in trees]
            # Tree is visible if there are only smaller trees on either side
            treesVisible += (maxHeight < currentTree).any()
            # Calculate scenic score
            # Scenic score is calculated by multiplying together number of visible trees on each side from the current tree
            scenicScores.append(
                np.prod([calculateVisibleTrees(currentTree, tree) for tree in trees])
            )

    print(f"Part 1 answer: {treesVisible}")
    print(f"Part 2 answer: {max(scenicScores)}")
