from DOTS import Dot


class Ship:
    def __init__(self, start, lives, position):
        self.start = start
        self.lives = lives
        self.position = position
        self.live_ship = lives

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.lives):
            point_x = self.start.x
            point_y = self.start.y

            if self.position == 0: #vertical position
                point_x += i

            elif self.position == 1: #horizontal position
                point_y += i

            ship_dots.append(Dot(point_x, point_y))

        return ship_dots

    def shot(self, shot):
        return shot in self.dots



