import numpy as np
import copy
from queue import Queue


def getElevation(item):
    # Return elevation value
    # 'a' = 0
    # ...
    # 'z' = 25
    return ord(item) - ord('a')


def splitRowToColumns(row):
    # Splits input string to list and converts items to elevation value starting at 0 for 'a'
    return [getElevation(item) for item in row.decode()]


def getAdjacentNodes(matrix, currentNode):
    # Return list of adjacent nodes in matrix (left, right, up, down)
    adjacentNodes = []
    if currentNode[0] > 0:
        adjacentNodes.append((currentNode[0]-1, currentNode[1]))
    if currentNode[0] < len(matrix) - 1:
        adjacentNodes.append((currentNode[0]+1, currentNode[1]))
    if currentNode[1] > 0:
        adjacentNodes.append((currentNode[0], currentNode[1]-1))
    if currentNode[1] < len(matrix[0]) - 1:
        adjacentNodes.append((currentNode[0], currentNode[1]+1))
    return adjacentNodes


def getAvailableNodes(matrix, currentNode, visitedNotes):
    # Return list on available nodes that meet the condition
    # (the elevation of the destination square can be at most one higher than the elevation of your current square)
    # and aren't already explored
    availableNodes = getAdjacentNodes(matrix, currentNode)
    availableNodes = [node for node in availableNodes if (
        node not in visitedNotes) and (matrix[node]-1 <= matrix[currentNode])]
    return availableNodes


def BFS(matrix, start, end):
    # Breadth-first search
    open = Queue()
    open.put([start])

    visited = []

    while not open.empty():
        currentNode = open.get()
        if currentNode[-1] in visited:
            continue
        if end is not None:
            # Part 1
            if currentNode[-1] == end:
                return currentNode
        else:
            # Part 2
            if matrix[currentNode[-1]] == getElevation('z'):
                return currentNode
        visited.append(currentNode[-1])
        for node in getAvailableNodes(matrix, currentNode[-1], visited):
            open.put(currentNode + [node])


if __name__ == "__main__":
    # Load input from file
    input = np.loadtxt("input.txt", dtype=list, converters=splitRowToColumns)
    # Convert input to numpy matrix
    matrix = np.array([row for row in input])

    # Get index of starting and ending position
    start = (np.where(matrix == getElevation('S'))[0][0],
             np.where(matrix == getElevation('S'))[1][0])
    end = (np.where(matrix == getElevation('E'))[0][0],
           np.where(matrix == getElevation('E'))[1][0])
    # Replace starting and ending position with given elevation
    matrix[matrix == getElevation('S')] = getElevation('a')
    matrix[matrix == getElevation('E')] = getElevation('z')

    part1 = len(BFS(matrix, start, end)) - 1
    print(f"Part 1 answer: {part1}")

    # Invert matrix for part 2 and find shortest path from top to bottom
    matrix2 = getElevation('z') - matrix
    part1 = len(BFS(matrix2, end, None)) - 1
    print(f"Part 1 answer: {part1}")
