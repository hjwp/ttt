from typing import List
from dataclasses import dataclass
from enum import Enum

class Rows(Enum):
    TOP = 1
    MIDDLE = 2
    BOTTOM = 3

class Cols(Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

@dataclass
class Position:
    col: Cols
    row: Rows



class Positions(list):
    def __init__(self, positions: List[Position]):
        super().__init__(positions)

    def __add__(self, other):
        return Positions(list(self) + other)

ALL_POSITIONS = [
    Position(c, r)
    for r in Rows
    for c in Cols
]


class Board:
    def __init__(self, Xs=None, Os=None):
        self.Xs = Positions(Xs or [])
        self.Os = Positions(Os or [])

    def draw(self):
        result = ''
        for p in ALL_POSITIONS:
            if p in self.Xs:
                result += 'X'
            elif p in self.Os:
                result += 'O'
            else:
                result += '.'
            if p.col is Cols.RIGHT:
                result += '\n'
        return result.strip()


    @property
    def state(self):
        rows = [
            [Position(Cols.LEFT,y), Position(Cols.MIDDLE,y), Position(Cols.RIGHT,y)]
            for y in Rows
        ]
        cols = [
            [Position(x,Rows.TOP), Position(x,Rows.MIDDLE), Position(x,Rows.BOTTOM)]
            for x in Cols
        ]
        diags = [
            [Position(Cols.LEFT,Rows.TOP), Position(Cols.MIDDLE,Rows.MIDDLE), Position(Cols.RIGHT,Rows.BOTTOM)],
            [Position(Cols.LEFT,Rows.BOTTOM), Position(Cols.MIDDLE,Rows.MIDDLE), Position(Cols.RIGHT,Rows.TOP)],
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
                Xs=Positions(self.Xs + [position]),
                Os=Positions(self.Os)
            )
        return Board(
            Xs=Positions(self.Xs),
            Os=Positions(self.Os + [position])
        )
