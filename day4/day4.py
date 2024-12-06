def checkX(txt, numchar, numrow):
    start_pos = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    count = 0
    for pos in start_pos:
        try:
            if txt[numrow + pos[1]][numchar + pos[0]] == 'M':
                if txt[numrow + pos[1] * 2][numchar + pos[0] * 2] == 'A' and numrow + pos[1] * 2 >= 0 and numchar + pos[0] * 2 >= 0:
                    if txt[numrow + pos[1] * 3][numchar + pos[0] * 3] == 'S' and numrow + pos[1] * 3 >= 0 and numchar + pos[0] * 3 >= 0:
                        count += 1
        except IndexError:
            continue
    print("Char: (", numchar, ', ', numrow, ") ;; Count: ", count)
    return count

def checkA(txt, numchar, numrow):
    positions = [[[-1, -1], [1, 1]], [[1, -1], [-1, 1]]]
    mas_count = 0
    for pos in positions:
        try:
            if txt[numrow + pos[0][1]][numchar + pos[0][0]] == 'M' and numrow + pos[0][1] >= 0 and numchar + pos[0][0] >= 0:
                if txt[numrow + pos[1][1]][numchar + pos[1][0]] == 'S' and numrow + pos[1][1] >= 0 and numchar + pos[1][0] >= 0:
                    mas_count += 1
            elif txt[numrow + pos[0][1]][numchar + pos[0][0]] == 'S' and numrow + pos[0][1] >= 0 and numchar + pos[0][0] >= 0:
                if txt[numrow + pos[1][1]][numchar + pos[1][0]] == 'M' and numrow + pos[1][1] >= 0 and numchar + pos[1][0] >= 0:
                    mas_count += 1
        except IndexError:
            continue
    if mas_count == 2:
        return True
    else:
        return False


def checkX(txt, numchar, numrow):
    start_pos = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    count = 0
    for pos in start_pos:
        try:
            if txt[numrow + pos[1]][numchar + pos[0]] == 'M':
                if txt[numrow + pos[1] * 2][numchar + pos[0] * 2] == 'A' and numrow + pos[1] * 2 >= 0 and numchar + pos[0] * 2 >= 0:
                    if txt[numrow + pos[1] * 3][numchar + pos[0] * 3] == 'S' and numrow + pos[1] * 3 >= 0 and numchar + pos[0] * 3 >= 0:
                        count += 1
        except IndexError:
            continue
    return count
            


def partOne(txt):
    count = 0
    for numrow, row in enumerate(txt):
        for numchar, char in enumerate(row):
            if char == 'X':
                count += checkX(txt, numchar, numrow)
    print(count)

def partTwo(txt):
    count = 0
    for numrow, row in enumerate(txt):
        for numchar, char in enumerate(row):
            if char == 'A':
                if checkA(txt, numchar, numrow) == True:
                    count += 1
    print(count)
    





with open("day4/input.txt", 'r') as inp:
    txt = inp.read().split('\n')

partOne(txt)
partTwo(txt)