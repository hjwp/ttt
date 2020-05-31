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



class Board:
    def __init__(self, Xs=None, Os=None):
        self.Xs = Positions(Xs or [])
        self.Os = Positions(Os or [])

    def draw(self):
        result = ''
        all_positions = [
            Position(c, r)
            for r in Rows
            for c in Cols
        ]
        for p in all_positions:
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
        complete_rows = [
            [Position(c, r) for c in Cols] for r in Rows
        ]
        complete_cols = [
            [Position(c, r) for r in Rows] for c in Cols
        ]
        diags = [
            [Position(c, r) for c, r in zip(Cols, Rows)],
            [Position(c, r) for c, r in zip(Cols, reversed(Rows))],
        ]

        for line in complete_rows + complete_cols + diags:
            if all(pos in self.Xs for pos in line):
                return 'X wins'
            if all(pos in self.Os for pos in line):
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
