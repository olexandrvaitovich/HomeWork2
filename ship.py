import random


class Ship:
    def __init__(self, length):
        self.length = length
        self.bow = (random.randint(1, 9), random.randint(1, 9))
        self.horizontal = random.choice((True, False))
        self.hit = [False in range(length)]

    def shoot_at(self, target):
        if self.horizontal == True:
            if target[0] in range(self.bow[0], self.bow[0]+self.length-1):
                self.hit[target[0]-self.bow[0]] = True
        else:
            if target[1] in range(self.bow[1], self.bow[1]+self.length-1):
                self.hit[target[1]-self.bow[1]] = True
        return self.hit
