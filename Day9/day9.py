import numpy as np
import itertools


def parseInstruction(line):
    # Parse instructions to list  with direction vectors
    # [1, 0] = move right, [0, -1] = move down, etc.
    directions = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}
    instructions = [directions[line[0]]] * line[1]
    return instructions


def getDirection(direction):
    # Normalize direction vector
    return 1 if direction > 0 else -1 if direction < 0 else 0


def moveTail(head, tail):
    distance = np.subtract(head, tail)
    if np.max(np.abs(distance)) >= 2:
        return np.add(tail, [getDirection(axis) for axis in distance])
    return tail


if __name__ == "__main__":
    # Load input from file, split row to two columns
    input = np.loadtxt("input.txt", dtype=list, delimiter=" ",
                       converters={1: lambda x: int(x)})
    # Parse instructions
    instructions = [parseInstruction(line) for line in input]
    instructions = list(itertools.chain.from_iterable(instructions))

    head = [0, 0]
    tail = []
    for i in range(9):
        tail.append([0, 0])

    visitedPositions1 = [tuple(tail[0])]
    visitedPositions2 = [tuple(tail[8])]

    for instruction in instructions:
        # Move head
        head = np.add(head, instruction)
        # Move tail
        tail[0] = moveTail(head, tail[0])
        for i in range(1, 9):
            tail[i] = moveTail(tail[i-1], tail[i])

        visitedPositions1.append(tuple(tail[0]))
        visitedPositions2.append(tuple(tail[8]))

    part1 = len(dict.fromkeys(visitedPositions1))
    print(f"Part 1 answer: {part1}")

    part2 = len(dict.fromkeys(visitedPositions2))
    print(f"Part 2 answer: {part2}")
