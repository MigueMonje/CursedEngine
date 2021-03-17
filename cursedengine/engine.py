from .math import Vector2
from .visuals import AsciiArt
import curses
import time

class DtTracker():
    @classmethod
    def start(cls):
        cls._t = time.time()*1000
    @classmethod
    def stop(cls):
        return time.time() *1000 - cls._t
class Thing():
    def __init__(self):
        pass
    
    def start(self,game):
        pass

    def update(self,dt,game):
        pass

    def render(self,stdscr):
        pass

    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return repr(self.__dict__)

class SpacialThing(Thing):
    cords:Vector2 = Vector2(0,0)
    def __init__(self,cords:Vector2):
        self.cords = cords

class ArtThing(SpacialThing):
    art:AsciiArt = None
    def __init__(self,cords:Vector2,art:AsciiArt):
        super().__init__(cords)
        self.art = art
    def render(self,stdscr):
        if self.art.transparent:
            dims = self.art.dim()
            for y in range(dims.y):
                for x in range(dims.x):
                    if self.art.lines[y][x] != " ":
                        stdscr.addstr(self.cords.y + y, self.cords.x + x, self.art.lines[y][x])
        else:
           # stdscr.addstr(self.cords.y,self.cords.x,str(self.art))
            for i in range(len(self.art.lines)):
                stdscr.addstr(self.cords.y + i,self.cords.x,self.art.lines[i])

class CharThing(SpacialThing):
    char:str = ""
    def __init__(self,cords:Vector2,char):
        super().__init__(cords)
        self.char = char
    def render(self,stdscr):
        stdscr.addstr(self.cords.y,self.cords.x,self.char)

class RectThing(SpacialThing):
    char:str = ""
    def __init__(self,cords:Vector2,dim:Vector2,char):
        super().__init__(cords)
        self.dim = dim
        self.char = char
    def render(self,stdscr):
        for y in range(self.cords.y, self.cords.y + self.dim.y):
            stdscr.addstr(y,self.cords.x,self.char * self.dim.x)


class Game:
    end = False
    key = None
    def __init__(self,*things,window):
        self.things = list(things)
        self.window = window
    def start(self):
        for thing in self.things:
            if isinstance(thing,Thing):
                thing.start(self)
            else:
                TypeError(f"{thing} is a {str(type(thing))}, not a Thing.")
    def loop(self):
        DtTracker.start()
        while True:
            self.window.clear()
            for thing in self.things:
                if isinstance(thing,Thing):
                    thing.update(DtTracker.stop(),self)
                    
                    thing.render(self.window)
                    
                else:
                    TypeError(f"{thing} is a {str(type(thing))}, not a Thing.")
            self.window.refresh()
            if self.end:
                break
            
            self.key = self.window.getkey()
                