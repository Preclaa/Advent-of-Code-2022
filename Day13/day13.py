import numpy as np
import json

RIGHT_ORDER = 1
WRONG_ORDER = 0
NO_ORDER = -1


def compare(left, right):
    # Recursively compare if pair is in the right order
    if type(left) == list and type(right) == int:
        return compare(left, [right])
    if type(left) == int and type(right) == list:
        return compare([left], right)
    if type(left) == list and type(right) == list:
        for i in range(min(len(left), len(right))):
            order = compare(left[i], right[i])
            if order != NO_ORDER:
                return order
        return RIGHT_ORDER if len(left) < len(right) else (WRONG_ORDER if len(left) > len(right) else NO_ORDER)
    else:
        return RIGHT_ORDER if left < right else (WRONG_ORDER if left > right else NO_ORDER)


if __name__ == "__main__":
    # Load input from file and parse it to lists
    input = [json.loads(row) for row in np.loadtxt("input.txt", dtype=list)]

    pairs = list(zip(input[::2], input[1::2]))

    part1 = 0
    for i, pair in enumerate(pairs):
        order = compare(pair[0], pair[1])
        # Add index to sum if it's in the right order (index starts at 1)
        if order == RIGHT_ORDER:
            part1 += i + 1

    print(f"Part 1 answer: {part1}")
