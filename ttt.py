from typing import List
from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int


class Positions(list):
    def __init__(self, positions: List[Position]):
        super().__init__(positions)

    def __add__(self, other):
        return Positions(list(self) + other)

    # def __lte__(self, other):
    #     return super().__lte__(list(other))


class Board:
    def __init__(self, Xs=None, Os=None):
        self.Xs = Positions(Xs or [])
        self.Os = Positions(Os or [])

    def draw(self):
        result = ''
        for y in range(3):
            for x in range(3):
                if Position(x, y) in self.Xs:
                    result += 'X'
                elif Position(x, y) in self.Os:
                    result += 'O'
                else:
                    result += '.'
            result += '\n'
        return result.strip()


    @property
    def state(self):
        rows = [[Position(0,y), Position(1,y), Position(2,y)] for y in range(3)]
        cols = [[Position(x,0), Position(x,1), Position(x,2)] for x in range(3)]
        diags = [
            [Position(0,0), Position(1,1), Position(2,2)],
            [Position(0,2), Position(1,1), Position(2,0)],
        ]

        for positions in rows + cols + diags:
            if all(pos in self.Xs for pos in positions):
                return 'X wins'
            if all(pos in self.Os for pos in positions):
                return 'O wins'
        if len(self.Xs + self.Os) == 9:
            return 'draw'
        return 'still playing'

    def take_turn(self, position):
        assert position not in self.Xs + self.Os
        if len(self.Xs) <= len(self.Os):
            return Board(
                Xs=Positions(self.Xs + [Position(position.x,position.y)]),
                Os=Positions(self.Os)
            )
        return Board(
            Xs=Positions(self.Xs),
            Os=Positions(self.Os + [Position(position.x, position.y)])
        )
