
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


    @property
    def state(self):
        rows = [[(0,y), (1,y), (2,y)] for y in range(3)]
        cols = [[(x,0), (x,1), (x,2)] for x in range(3)]
        diags = [
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)],
        ]

        for positions in rows + cols + diags:
            if all(pos in self.Xs for pos in positions):
                return 'X wins'
            if all(pos in self.Os for pos in positions):
                return 'O wins'
        if len(self.Xs + self.Os) == 9:
            return 'draw'
        return 'still playing'

    def take_turn(self, x, y):
        assert (x,y) not in self.Xs + self.Os
        if self.Xs <= self.Os:
            return Board(self.Xs + [(x,y)], self.Os)
        return Board(self.Xs, self.Os + [(x, y)])
