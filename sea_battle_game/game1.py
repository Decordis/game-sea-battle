from random import randint

from DOTS import Dot
from Ship import Ship
from board import Board
from mists import BoardWrongShipException
from player import User, AI


class Game:

    def __init__(self, lots=6):
        self.lots = lots
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)
    def try_board(self):
        _lens_ = [3, 2, 2, 1, 1, 1, 1]
        board = Board(lots = self.lots)
        for i in _lens_:
            try_ = 0
            while True:
                try_ += 1
                if try_ == 1000:
                    return None
                ship = Ship(Dot(randint(0, self.lots-1), randint(0, self.lots-1)), i, randint(0,1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass

        board.start()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("------------------------------------")
        print("Hello there in the game 'Warship' :)")
        print("------------------------------------")
        print(" Format: x y ")
        print("x - number string  ")
        print("y - number column ")
        print("When u will kill the ship")
        print("U will see contour of ship by '+' ")
        print("------------------------------------")
        print("Good luck! ")


    def loop(self):
        num = 0
        while True:
            print("User board:")
            self.us.board.get_board()
            print("AI board:")
            self.ai.board.get_board()
            if num % 2 == 0:
                print("User move!")
                repeat = self.us.move()
            else:
                print("AI move!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.attempt == 7:
                print("User have won!!")
                close = input("Click 'Enter' to close")
                break

            if self.us.board.attempt == 7:
                print("AI have won!!")
                close1 = input("Click 'Enter' to close")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

