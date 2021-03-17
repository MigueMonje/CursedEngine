from cursedengine.engine import Game
from things import Icon
from curses import wrapper
def main(stdscr):
    game = Game(
        Icon(),
        window = stdscr
    )
    game.start()
    game.loop()
wrapper(main)