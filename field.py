from ship import Ship


class Field:
    def __init__(self):
        self = self

    def ships(self):
        lst = [[' ' for i in range(14)] for i in range(14)]
        lst_with_ships = self.one(self.two(self.three(self.four(lst))))
        final_lst = [i[2:12] for i in lst_with_ships[2:12]]
        st = ''
        for i in final_lst:
            for j in i:
                st += j
            st += '\n'
        return st

    def ok(self, lst):
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
        return lst

    def four(self, lst):
        ship = Ship(4)
        while ship.bow[0]+2 > 8 or ship.bow[1]+2 > 8:
            ship = Ship(4)
        lst[ship.bow[1]+2][ship.bow[0]+2] = '*'
        if ship.horizontal == True:
            lst[ship.bow[1]+2][ship.bow[0]+3] = '*'
            lst[ship.bow[1]+2][ship.bow[0]+4] = '*'
            lst[ship.bow[1]+2][ship.bow[0]+5] = '*'
        else:
            lst[ship.bow[1]+3][ship.bow[0]+2] = '*'
            lst[ship.bow[1]+4][ship.bow[0]+2] = '*'
            lst[ship.bow[1]+5][ship.bow[0]+2] = '*'
        lst = self.ok(lst)
        return lst

    def three(self, lst):
        for i in range(2):
            ship = Ship(3)
            n = 0
            while n == 0:
                ship = Ship(3)
                if ship.bow[0]+2 < 10 and ship.bow[1]+2 < 10 and lst[ship.bow[1]+2][ship.bow[0]+2] == ' ':
                    if ship.horizontal == True:
                        if lst[ship.bow[1]+2][ship.bow[0]+4] == ' ':
                            lst[ship.bow[1]+2][ship.bow[0]+2] = '*'
                            lst[ship.bow[1]+2][ship.bow[0]+3] = '*'
                            lst[ship.bow[1]+2][ship.bow[0]+4] = '*'
                            n = 1
                    else:
                        if lst[ship.bow[1]+4][ship.bow[0]+2] == ' ':
                            lst[ship.bow[1]+2][ship.bow[0]+2] = '*'
                            lst[ship.bow[1]+3][ship.bow[0]+2] = '*'
                            lst[ship.bow[1]+4][ship.bow[0]+2] = '*'
                            n = 1
            lst = self.ok(lst)
        return lst

    def two(self, lst):
        for i in range(3):
            ship = Ship(2)
            n = 0
            while n == 0:
                ship = Ship(2)
                if ship.bow[0]+2 < 11 and ship.bow[1]+2 < 11 and lst[ship.bow[1]+2][ship.bow[0]+2] == ' ':
                    if ship.horizontal == True:
                        if lst[ship.bow[1]+2][ship.bow[0]+3] == ' ':
                            lst[ship.bow[1]+2][ship.bow[0]+2] = '*'
                            lst[ship.bow[1]+2][ship.bow[0]+3] = '*'
                            n = 1
                    else:
                        if lst[ship.bow[1]+3][ship.bow[0]+2] == ' ':
                            lst[ship.bow[1]+2][ship.bow[0]+2] = '*'
                            lst[ship.bow[1]+3][ship.bow[0]+2] = '*'
                            n = 1
            lst = self.ok(lst)
        return lst

    def one(self, lst):
        for i in range(4):
            ship = Ship(1)
            while lst[ship.bow[1]+2][ship.bow[0]+2] != ' ':
                ship = Ship(1)
            lst[ship.bow[1]+2][ship.bow[0]+2] = '*'
            lst = self.ok(lst)
        return lst
