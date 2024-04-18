from DOTS import Dot
from mists import BoardOutException, BoardUsedException, BoardWrongShipException


class Board:
    def __init__(self, hid=False, lots=6):
        self.field = [["O"] * lots for i in range(lots)]
        self.ships = []
        self.hid = hid
        self.busy = []
        self.lots = lots
        self.attempt = 0

    def get_board(self):
        print()
        box_str = ""
        box_str += "       1  |  2  |  3  |  4  |  5  |  6  |"
        print(box_str)
        print("-----------------------------------------")
        for i, row in enumerate(self.field):
            box_str = f" {i+1}  |  {'  |  '.join(row)}  |"
            if self.hid:
                box_str = box_str.replace("■", "O")
            print(box_str)
            print("-----------------------------------------")
        print()



    def out(self, d):
        return not ((0 <= d.x < self.lots and 0<=d.y<self.lots))

    def contour(self, ship, verb = False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                poi = Dot(d.x + dx, d.y + dy)
                # self.field[poi.x][poi.y] = "+"
                if not (self.out(poi)) and poi not in self.busy:
                    if verb:
                        self.field[poi.x][poi.y] = "+"
                    self.busy.append(poi)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()
        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.live_ship -= 1
                self.field[d.x][d.y] = "X"
                if ship.live_ship == 0:
                    self.attempt += 1
                    self.contour(ship, verb=True)
                    print("The Ship has been killed!")
                    return False
                else:
                    print("The Ship is injured!")
                    return True

        self.field[d.x][d.y] = "-"
        print("Miss!")
        return False

    def start(self):
        self.busy = []
