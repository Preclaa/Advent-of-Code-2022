import numpy as np
import itertools


def convertInstruction(instruction):
    # Convert instruction to the list with values
    # Instruction noop does nothing and takes 1 cycle, so it converts to [0]
    # Instruction addx increses register value after 2 cycles, so it converts to [0, value]
    return [0] if instruction.startswith("noop") else [0, int(instruction.split(" ")[1])]


if __name__ == "__main__":
    # Read input from file
    with open("input.txt") as input:
        lines = [line.rstrip() for line in input]

    # Parse instructions from input
    instructions = [convertInstruction(instruction) for instruction in lines]
    instructions = list(itertools.chain(*instructions))

    # List containing values of register in each cycle
    register = np.ones(len(instructions), dtype=int)
    crt = []
    for i, instruction in enumerate(instructions):
        # Increment value of register for the next cycle
        register[i+1::] = np.add(register[i], instruction)
        # Draw pixel if the sprite is visible
        crt.append("#" if i % 40 in range(
            register[i]-1, register[i]+2) else ".")

    # Calculate sum of the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles
    signalSum = 0
    for i, value in enumerate(register[19:220:40]):
        signalSum += value * (20 + i * 40)

    print(f"Part 1 answer: {signalSum}")
    print("Part 2 answer:")
    for i in range(6):
        print(''.join(map(str, crt[i*40:(i*40)+40])))
