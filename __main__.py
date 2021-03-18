from cursedengine.engine import Game, Cursor
from cursedengine.math import Vector2
import things
import curses
def main(stdscr):
    game = Game(
        things.Icon(),
        Cursor(Vector2(0,0)),
        window = stdscr,
        curses= curses
    )
    game.start()
    game.loop()
curses.wrapper(main)