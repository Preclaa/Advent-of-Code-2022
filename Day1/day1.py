import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as input:
        # Load input from file and replace empty lines to -1
        inputLines = [-1 if i == '\n' else int(i) for i in input.readlines()]
        # Append -1 (Separator) to the end
        inputLines.append(-1)
        # Convert to numpy array
        lines = np.asarray(inputLines)

        sum = np.empty(0, dtype=int)
        temp = 0
        for line in lines:
            if line == -1:
                sum = np.append(sum, temp)
                temp = 0
            else:
                temp += line

        # Sort array from largest to smallest number
        sum = np.sort(sum)[::-1]

        part1 = sum[0]
        part2 = np.sum(sum[0:3])

        print(f"Part 1 answer: {part1}")
        print(f"Part 2 answer: {part2}")
