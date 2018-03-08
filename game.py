from field import Field
from player import Player
from ship import Ship


class Game:
    def __init__(self, players, fields, current_player):
        self.players = players
        self.fields = fields
        self.current_player = current_player

    def read_position(self, shot):
        return (chr(shot[0]-65, shot[1]))

    def field_without_ships(self, index):
        return self.fields[index].replace('*', ' ').replace('-', ' ')

    def field_with_ships(self, index):
        return self.fields[index]
