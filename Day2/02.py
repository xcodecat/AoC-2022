def part_1():
    file = open("Day2/02.txt", "r")
    score = 0
    for line in file:
        p, me = line.replace("\n", "").split(" ")
        if me == "X":
            score += 1
        elif me =="Y":
            score += 2
        else:
            score += 3
        if ord(me) - ord(p) == 23:
            score += 3
        elif ord(me) - ord(p) == 24 or ord(me) - ord(p) == 21:
            score += 6
    print("Part2:", score)
part_1()

def resultat(tmp_resultat):
    if tmp_resultat == 88 or tmp_resultat > 90:
        return 1
    elif tmp_resultat == 89:
        return 2
    elif tmp_resultat == 90 or tmp_resultat < 88:
        return 3

def part_2():
    file = open("Day2/02.txt", "r")
    score = 0
    for line in file:
        p, me = line.replace("\n","").split(" ")        
        if me == "Y":
            score += resultat(ord(p) + 23) + 3
        elif me == "Z":
            score += resultat(ord(p) + 24) + 6
        else:
            score += resultat(ord(p) + 22)
    print("Part2:", str(score))
part_2()