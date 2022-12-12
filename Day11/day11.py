import numpy as np
import copy


def play(monkeys, rounds, lcm):
    for _ in range(rounds):
        for monkey in monkeys:
            monkey[4] += len(monkey[0])
            while monkey[0]:
                old = monkey[0].pop()
                new = int(
                    eval(monkey[1]) / 3) if rounds == 20 else int(eval(monkey[1]) % lcm)
                monkeys[monkey[3][new % monkey[2] != 0]][0].append(new)
    # Multiply top two total number of times each monkey inspects items
    return np.product(np.sort([monkey[4] for monkey in monkeys])[::-1][:2])


if __name__ == "__main__":
    # Read input from file
    with open("input.txt") as input:
        lines = [line.rstrip() for line in input]

    # Parse input
    items = [list(map(int, line.split(":")[1].split(",")))
             for line in lines[1::7]]
    operations = [line.split("=")[1] for line in lines[2::7]]
    tests = [int(line.split(" ")[-1])
             for line in lines[3::7]]
    testResults = list(zip([int(line.split(" ")[-1])for line in lines[4::7]],
                           [int(line.split(" ")[-1])for line in lines[5::7]]))

    inspectedItems = [0 for _ in range(len(items))]
    # Create monkeys by zipping input values
    monkeys = zip(items, operations, tests, testResults, inspectedItems)
    # Convert list of tuples to list of lists
    monkeys = [list(monkey) for monkey in monkeys]
    monkeys2 = copy.deepcopy(monkeys)  # Copy for part 2

    # Calculate least common multiple for part 2
    lcm = np.lcm.reduce(tests)

    part1 = play(monkeys, 20, lcm)
    print(f"Part 1 answer: {part1}")
    part2 = play(monkeys2, 10000, lcm)
    print(f"Part 2 answer: {part2}")
