class Player:
    def __init__(self, name):
        self.name = name

    def read_position(self, shot):
        return (chr(shot[0]-65, shot[1]))