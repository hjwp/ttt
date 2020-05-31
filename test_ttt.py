import pytest
from textwrap import dedent
from ttt import Board, Position, Positions

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
    board = board.take_turn(Position(0,0))
    assert board.draw() == dedent("""
        X..
        ...
        ...
        """).strip()

def test_take_turn_handles_x_and_y():
    board = Board()
    board = board.take_turn(Position(1,1))
    assert board.draw() == dedent("""
        ...
        .X.
        ...
        """).strip()

def test_take_turn_handles_x():
    board = Board()
    board = board.take_turn(Position(2,0))
    assert board.draw() == dedent("""
        ..X
        ...
        ...
        """).strip()


def test_take_turn_handles_y():
    board = Board()
    board = board.take_turn(Position(0,2))
    assert board.draw() == dedent("""
        ...
        ...
        X..
        """).strip()


def test_second_turn_is_O():
    board0 = Board()
    board1 = board0.take_turn(Position(1,1))
    board2 = board1.take_turn(Position(2,2))
    assert board2.draw() == dedent("""
        ...
        .X.
        ..O
        """).strip()

def test_third_turn():
    board0 = Board()
    board1 = board0.take_turn(Position(1,1))
    board2 = board1.take_turn(Position(2,2))
    board3 = board2.take_turn(Position(0,2))
    assert board3.draw() == dedent("""
        ...
        .X.
        X.O
        """).strip()


def test_cannot_play_on_already_played_position():
    board0 = Board()
    board1 = board0.take_turn(Position(1,1))
    with pytest.raises(Exception):
        board1.take_turn(Position(1,1))


def test_win_horizonal_X():
    board = Board(Xs=Positions([Position(0,0), Position(1,0), Position(2,0)]))
    print(board.draw())
    assert board.state == 'X wins'


def test_win_horizonal_O():
    board = Board(Os=Positions([Position(0,0), Position(1,0), Position(2,0)]))
    print(board.draw())
    assert board.state == 'O wins'

def test_win_vertical_X():
    board = Board(Xs=Positions([Position(0,0), Position(0,1), Position(0,2)]))
    print(board.draw())
    assert board.state == 'X wins'

def test_win_vertical_O():
    board = Board(Os=Positions([Position(0,0), Position(0,1), Position(0,2)]))
    print(board.draw())
    assert board.state == 'O wins'

def test_win_diagonal_X():
    board = Board(Xs=Positions([Position(0,0), Position(1,1), Position(2,2)]))
    print(board.draw())
    assert board.state == 'X wins'

def test_win_diagonal_O():
    board = Board(Os=Positions([Position(2,0), Position(1,1), Position(0,2)]))
    print(board.draw())
    assert board.state == 'O wins'


@pytest.mark.skip()
def test_draw():
    ...
    assert board.state == 'draw'
