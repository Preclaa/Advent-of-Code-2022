import numpy as np


def getLetterPriority(letter):
    # Get letter priority:
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    return ord(letter) - (ord('a') - 1 if letter.islower()
                          else ord('A') - 1 - 26)


def filterRucksack(rucksack):
    rucksack = rucksack.decode()
    # Convert string with items to array with priority of each item
    return [getLetterPriority(letter) for letter in rucksack]


@np.vectorize
def getSharedItem(rucksack):
    # Split array in half
    rucksack = np.array_split(rucksack, 2)
    # Find the item type that appears in both compartments
    return np.intersect1d(rucksack[0], rucksack[1])


def getGroupBadge(group):
    # Find the item type that appears in every rucksack of the group
    return np.intersect1d(np.intersect1d(group[0], group[1]), group[2])


if __name__ == "__main__":
    # Load input from file and find the priority of shared item in both compartments
    input = np.loadtxt("input.txt", dtype=list,
                       converters={0: lambda x: filterRucksack(x)})

    part1 = np.sum(getSharedItem(input))
    print(f"Part 1 answer: {part1}")

    # Split array to groups of 3
    groups = np.array_split(input, np.size(input)/3)
    part2 = np.sum([getGroupBadge(group) for group in groups])
    print(f"Part 2 answer: {part2}")
