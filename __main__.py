from cursedengine.engine import Game
import things
from curses import wrapper
def main(stdscr):
    game = Game(
        things.Icon(),
        window = stdscr
    )
    game.start()
    game.loop()
wrapper(main)