file = open("Day1/01.txt")

def function():
    product = [0]
    i = 0
    for line in file:
        if line == "\n":
            i += 1
            product.append(0)
        else:
            product[i] += int(line)
    return product

def part1():
    product = function()
    print("Part1: ", str(max(product)))

def part2():
    product = function()
    print("Part2: ", str(sum(sorted(product, reverse=True)[:3])))

#part1()
part2()