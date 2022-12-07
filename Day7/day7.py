import os
from pathlib import Path
import numpy as np


def calculateDirectorySize(directories, path):
    # Calculates total size of directory with its subdirectories
    subdirectories = [
        calculateDirectorySize(directories, subdir) for subdir in directories[path][0]
    ]
    return int(directories[path][1] + np.sum(subdirectories))


if __name__ == "__main__":
    # Read input from file
    with open("input.txt") as input:
        input = [line.rstrip() for line in input]

    directories = {}
    currentDir = "/"
    for line in input:
        # Execute cd command
        if line.startswith("$ cd"):
            # Move by one level up
            if line[5:] == "..":
                currentDir = str(Path(currentDir).parents[0])
            # Initialize list for given directory
            # First element in list is list with subdirectories
            # Second element is total sum of file sizes in directory
            else:
                currentDir = os.path.join(currentDir, line[5:])
                directories[currentDir] = [[], 0]
        # Add subdirectory to the list of subdirectories of current directory
        if line.startswith("dir"):
            directories[currentDir][0].append(os.path.join(currentDir, line[4:]))
        # Add size of file to the sum of current directory
        if line[0].isdigit():
            directories[currentDir][1] += int(line.split(" ")[0])

        # Line with "$ ls" is ignored

    # Calculate size for every directory
    directoriesSize = [
        calculateDirectorySize(directories, dir) for dir in directories.keys()
    ]

    # Calculate sum of every directory smaller than 100000
    part1 = np.sum([size for size in directoriesSize if size <= 100000])
    print(f"Part 1 answer: {part1}")

    totalSpace = 70000000
    neededSpace = 30000000
    usedSpace = calculateDirectorySize(directories, "/")
    spaceToFree = neededSpace - (totalSpace - usedSpace)

    # Calculate smallest directory size that is bigger than space needed to free
    part2 = np.sort([size for size in directoriesSize if size >= spaceToFree])[0]
    print(f"Part 2 answer: {part2}")
