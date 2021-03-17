from cursedengine.math import Vector2
from cursedengine.visuals import AsciiArt
from cursedengine.engine import Thing, SpacialThing, ArtThing, CharThing, RectThing, Game
class Icon(ArtThing):
    def __init__(self):
        self.art = AsciiArt.fromFile("cursedengine/icon.txt")
        self.cords = Vector2(5,5)
    def update(self,_,game:Game):
        if game.key == "e":
            game.end = True
    