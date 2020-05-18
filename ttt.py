
class Board:
    def __init__(self, Xs=None, Os=None):
        self.Xs = Xs or []
        self.Os = Os or []

    def draw(self):
        result = ''
        for y in range(3):
            for x in range(3):
                if (x, y) in self.Xs:
                    result += 'X'
                elif (x, y) in self.Os:
                    result += 'O'
                else:
                    result += '.'
            result += '\n'
        return result.strip()

    def take_turn(self, x, y):
        if self.Xs <= self.Os:
            return Board(self.Xs + [(x,y)], self.Os)
        return Board(self.Xs, self.Os + [(x, y)])

