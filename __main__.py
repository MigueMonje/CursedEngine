from cursedengine.engine import Game, Cursor
from cursedengine.math import Vector2
import things
from curses import wrapper
def main(stdscr):
    game = Game(
        things.Icon(),
        Cursor(Vector2(0,0)),
        window = stdscr
    )
    game.start()
    game.loop()
wrapper(main)