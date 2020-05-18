from textwrap import dedent
import ttt

def test_starting_board():
    board = ttt.Board()
    assert board.draw() == dedent("""
        ...
        ...
        ...
        """).strip()

