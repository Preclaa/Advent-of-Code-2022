from collections import Counter

def checkOccurrences(substring):
    # Checks if every character in substring is different
    return Counter(substring).most_common(1)[0][1] == 1

if __name__ == "__main__":
    # Read input from file
    with open("input.txt") as input:
        input = [line.rstrip() for line in input][0]
    position = 0
    # Find start-of-packet
    while len(input[position:position+4]) == 4:
        if checkOccurrences(input[position:position+4]):
            print(f"Part 1 answer: {position + 4}")
            position += 4
            break
        position += 1
    # Find start-of-message
    while len(input[position:position+14]) == 14:
        if checkOccurrences(input[position:position+14]):
            print(f"Part 2 answer: {position + 14}")
            break
        position += 1
    