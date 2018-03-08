import random


def read_file(filename, file_w):
    lst = []
    n = 97
    k = 1
    f = open(filename, 'r').readlines()
    for i in f:
        k = 1
        for j in i:
            lst.append(
                (chr(n), str(k), ('void' if j == ' ' else ('s' if j == '*' else 'p'))))
            #k += 1
        n += 1
    for i in lst:
        file_w.write(i)


def is_valid(field):
    f = open(field, 'r').readlines()
    if len(f) != 10:
        return False
    for i in f:
        if len(i) != 10:
            return False
    return True


def field_to_str(field):
    string = ''
    f = open(field, 'r').readlines()
    for i in f:
        string += i[0]+i[1]+i[2]+'\n'
    return string


def has_ship(field, place):
    f = open(field, 'r').readlines()
    for i in f:
        if place[0] in i and str(place[1]) in i:
            if i[2] != 'sea':
                return True
    return False


def ship_size(field, place):
    f = open(field, 'r').readlines()
    n = 1
    k = 1
    if has_ship(field, place) == False:
        return 'No ship'
    for i in f:
        if (chr(ord(place[0])+1) in i and place[1] in i) or (chr(ord(place[0])-1) in i and place[1] in i):
            k += 1
            if (chr(ord(place[0])+2) in i and place[1] in i) or (chr(ord(place[0])-2) in i and place[1] in i):
                k += 1
                if (chr(ord(place[0])+3) in i and place[1] in i) or (chr(ord(place[0])-3) in i and place[1] in i):
                    k += 1
        if (place[0] in i and place[1]+1 in i) or(place[0] in i and place[1]-1 in i):
            n += 1
            if (place[0] in i and place[1]+2 in i) or(place[0] in i and place[1]-2 in i):
                n += 1
                if (place[0] in i and place[1]+3 in i) or(place[0] in i and place[1]-3 in i):
                    n += 1
    return (n, k)


def generate_field():
    lst = [[' ' for i in range(14)] for i in range(14)]
    count = 1
    a = random.randint(2, 11)
    b1 = random.randint(2, 11)
    lst[a][b1] = '*'
    if b1 < 7:
        lst[a][b1+1] = '*'
        lst[a][b1+2] = '*'
        lst[a][b1+3] = '*'
    else:
        lst[a][b1-1] = '*'
        lst[a][b1-2] = '*'
        lst[a][b1-3] = '*'

    def ok():
        for i in range(13):
            for j in range(13):
                if lst[i][j] == '*':
                    lst[i][j+1] = '-' if lst[i][j+1] == ' ' else lst[i][j+1]
                    lst[i][j-1] = '-' if lst[i][j-1] == ' ' else lst[i][j-1]
                    lst[i+1][j+1] = '-' if lst[i+1][j +
                                                    1] == ' ' else lst[i+1][j+1]
                    lst[i-1][j-1] = '-' if lst[i-1][j -
                                                    1] == ' ' else lst[i-1][j-1]
                    lst[i+1][j] = '-' if lst[i+1][j] == ' ' else lst[i+1][j]
                    lst[i-1][j] = '-' if lst[i-1][j] == ' ' else lst[i-1][j]
                    lst[i+1][j-1] = '-' if lst[i+1][j -
                                                    1] == ' ' else lst[i+1][j-1]
                    lst[i-1][j+1] = '-' if lst[i-1][j +
                                                    1] == ' ' else lst[i-1][j+1]

    ok()
    for i in range(2):
        while lst[a][b1] != ' ':
            a = random.randint(2, 11)
            b1 = random.randint(2, 11)
        c = 0
        if lst[a][b1+1] == ' ':
            if lst[a][b1+2] == ' ':
                if b1 in range(2, 10):
                    lst[a][b1] = '*'
                    lst[a][b1+1] = '*'
                    lst[a][b1+2] = '*'
                    c = 1
        if c == 0:
            if lst[a][b1-1] == ' ':
                if lst[a][b1-2] == ' ':
                    if b1 in range(4, 11):
                        lst[a][b1] = '*'
                        lst[a][b1-1] = '*'
                        lst[a][b1-2] = '*'
                        c = 1
        if c == 0:
            if lst[a+1][b1] == ' ':
                if lst[a+2][b1] == ' ':
                    if a in range(2, 10):
                        lst[a][b1] = '*'
                        lst[a+1][b1] = '*'
                        lst[a+2][b1] = '*'
                        c = 1
        if c == 0:
            if lst[a-1][b1] == ' ':
                if lst[a-2][b1] == ' ':
                    if a in range(4, 11):
                        lst[a][b1] = '*'
                        lst[a-1][b1] = '*'
                        lst[a-2][b1] = '*'

        ok()
    for i in range(3):
        while lst[a][b1] != ' ':
            a = random.randint(2, 11)
            b1 = random.randint(2, 11)
        c = 0
        if lst[a][b1+1] == ' ':
            if b1 in range(2, 11):
                lst[a][b1] = '*'
                lst[a][b1+1] = '*'
                c = 1
        if c == 0:
            if lst[a][b1-1] == ' ':
                if b1 in range(3, 11):
                    lst[a][b1] = '*'
                    lst[a][b1-1] = '*'
                    c = 1
        if c == 0:
            if lst[a+1][b1] == ' ':
                if a in range(2, 11):
                    lst[a][b1] = '*'
                    lst[a+1][b1] = '*'
                    c = 1
        if c == 0:
            if lst[a-1][b1] == ' ':
                if a in range(3, 11):
                    lst[a][b1] = '*'
                    lst[a-1][b1] = '*'
        ok()
    for i in range(4):
        while lst[a][b1] != ' ':
            a = random.randint(2, 11)
            b1 = random.randint(2, 11)
        lst[a][b1]='*'   
        ok()
    final_lst=[i[2:12] for i in lst[2:12]]
    return final_lst
