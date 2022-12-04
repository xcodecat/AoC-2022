def to_number(char):
    char = ord(char)
    if char < 91:
        return char - 38
    else:
        return char - 96

def part_1():
    file = open("Day3/03.txt", "r")
    types = 0
    for line in file:
        item_1 = line[:int(len(line)/2)]
        item_2 = line[int(len(line)/2):]
        for c in item_1:
            if c in item_2:
                types += to_number(c)
                break
    print("Part1:", str(types))
part_1()

def part_2():
    file = [line for line in open("Day3/03.txt", "r")]
    types = 0
    for i in range(0, len(file), 3):
        for c in file[i]:
            if c in file[i+1] and c in file[i+2]:
                types += to_number(c)
                break
    print("Part2:", str(types))
part_2()