import numpy as np
import copy

if __name__ == "__main__":
    # Read input from file
    with open("input.txt") as input:
        lines = [line.rstrip() for line in input]
    
    # Parse stack input
    stackInput = [line for line in lines if line.startswith("[")]
    # Parse instructions
    instructions = [line for line in lines if line.startswith("move")]
    instructions = np.loadtxt(instructions, dtype=int, usecols=(1,3,5))
    
    # Get number of columns/stacks in input
    stackSize = np.loadtxt([line for line in lines if line.startswith(" 1")], dtype=int).max()
    
    # Initialize list of stacks
    stack1 = []
    for i in range(stackSize):
        stack1.append([])
    
    # Add values to stacks
    for line in stackInput[::-1]:
        for i, j in enumerate(range(1, len(line), 4)):
            if line[j] != " ":
                stack1[i].append(line[j])
    
    # Create copy of stack for part 2
    stack2 = copy.deepcopy(stack1)
            
    # Execute instructions
    for instruction in instructions:
        crates = []
        for i in range(instruction[0]):
            stack1[instruction[2] - 1].append(stack1[instruction[1] - 1].pop())
            # Load values from stack for part 2
            crates.append(stack2[instruction[1] - 1].pop())
        for i in range(instruction[0]):
            stack2[instruction[2] - 1].append(crates.pop())
            
    part1 = ""
    for x in stack1:
        part1 += x.pop()
    print(f"Part 1 answer: {part1}")
    
    part2 = ""
    for x in stack2:
        part2 += x.pop()
    print(f"Part 1 answer: {part2}")

