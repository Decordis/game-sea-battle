from random import randint

from DOTS import Dot
from mists import BoardException


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                point = self.ask()
                repeat = self.enemy.shot(point)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Dot(randint(0,5), randint(0, 5))
        print(f"AI move: {d.x+1} {d.y+1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Numbers").split()
            if len(cords) != 2:
                print("Need 2 nums")
                continue

            x, y = cords

            if not (x.isdigit()) and (y.isdigit()):
                print("We use only numbers!!")
                continue

            x, y = int(x), int(y)

            return Dot(x-1, y-1)
