import pytest
from textwrap import dedent
from ttt import Board, Cols, Position, Positions, Rows

def test_starting_board():
    board = Board()
    assert board.draw() == dedent("""
        ...
        ...
        ...
        """).strip()
    assert board.state == 'still playing'

def test_first_turn_is_X():
    board = Board()
    board = board.take_turn(Position(Cols.LEFT,Rows.TOP))
    assert board.draw() == dedent("""
        X..
        ...
        ...
        """).strip()

def test_take_turn_handles_x_and_y():
    board = Board()
    board = board.take_turn(Position(Cols.MIDDLE,Rows.MIDDLE))
    assert board.draw() == dedent("""
        ...
        .X.
        ...
        """).strip()

def test_take_turn_handles_x():
    board = Board()
    board = board.take_turn(Position(Cols.RIGHT,Rows.TOP))
    assert board.draw() == dedent("""
        ..X
        ...
        ...
        """).strip()


def test_take_turn_handles_y():
    board = Board()
    board = board.take_turn(Position(Cols.LEFT,Rows.BOTTOM))
    assert board.draw() == dedent("""
        ...
        ...
        X..
        """).strip()


def test_second_turn_is_O():
    board0 = Board()
    board1 = board0.take_turn(Position(Cols.MIDDLE,Rows.MIDDLE))
    board2 = board1.take_turn(Position(Cols.RIGHT,Rows.BOTTOM))
    assert board2.draw() == dedent("""
        ...
        .X.
        ..O
        """).strip()

def test_third_turn():
    board0 = Board()
    board1 = board0.take_turn(Position(Cols.MIDDLE,Rows.MIDDLE))
    board2 = board1.take_turn(Position(Cols.RIGHT,Rows.BOTTOM))
    board3 = board2.take_turn(Position(Cols.LEFT,Rows.BOTTOM))
    assert board3.draw() == dedent("""
        ...
        .X.
        X.O
        """).strip()


def test_cannot_play_on_already_played_position():
    board0 = Board()
    board1 = board0.take_turn(Position(Cols.MIDDLE,Rows.MIDDLE))
    with pytest.raises(Exception):
        board1.take_turn(Position(Cols.MIDDLE,Rows.MIDDLE))


def test_win_horizonal_X():
    board = Board(Xs=Positions([Position(Cols.LEFT,Rows.TOP), Position(Cols.MIDDLE,Rows.TOP), Position(Cols.RIGHT,Rows.TOP)]))
    print(board.draw())
    assert board.state == 'X wins'


def test_win_horizonal_O():
    board = Board(Os=Positions([Position(Cols.LEFT,Rows.TOP), Position(Cols.MIDDLE,Rows.TOP), Position(Cols.RIGHT,Rows.TOP)]))
    print(board.draw())
    assert board.state == 'O wins'

def test_win_vertical_X():
    board = Board(Xs=Positions([Position(Cols.LEFT,Rows.TOP), Position(Cols.LEFT,Rows.MIDDLE), Position(Cols.LEFT,Rows.BOTTOM)]))
    print(board.draw())
    assert board.state == 'X wins'

def test_win_vertical_O():
    board = Board(Os=Positions([Position(Cols.LEFT,Rows.TOP), Position(Cols.LEFT,Rows.MIDDLE), Position(Cols.LEFT,Rows.BOTTOM)]))
    print(board.draw())
    assert board.state == 'O wins'

def test_win_diagonal_X():
    board = Board(Xs=Positions([Position(Cols.LEFT,Rows.TOP), Position(Cols.MIDDLE,Rows.MIDDLE), Position(Cols.RIGHT,Rows.BOTTOM)]))
    print(board.draw())
    assert board.state == 'X wins'

def test_win_diagonal_O():
    board = Board(Os=Positions([Position(Cols.RIGHT,Rows.TOP), Position(Cols.MIDDLE,Rows.MIDDLE), Position(Cols.LEFT,Rows.BOTTOM)]))
    print(board.draw())
    assert board.state == 'O wins'


@pytest.mark.skip()
def test_draw():
    ...
    assert board.state == 'draw'
