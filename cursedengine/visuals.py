from .math import Vector2

class AsciiArt:
    Fixed = False
    def fix(self):
        mxlen = 0
        for i in self.lines:
            if len(i) > mxlen:
                mxlen = len(i)
        self.lines = [i + " " * (mxlen-len(i)) for i in self.lines]
        self.Fixed = True

    def __init__(self,*lines,t = False, fix = True):
        self.lines = list(lines)
        self.transparent = t
        if fix:
            self.fix()
    
    def dim(self):
        if self.Fixed:
            return Vector2(len(self.lines[0]),len(self.lines))
        else:
            return Exception("Cannot get dimencions of unfixed AsciiArt")

    def section(self,f:Vector2,to:Vector2):
        if self.Fixed:
            ySection = self.lines[f.y:to.y]
            section = [i[f.x:to.x] for i in ySection]
            return AsciiArt(*section,t=self.transparent)
        else:
            return Exception("Cannot take a section of unfixed AsciiArt")

    def __str__(self):
        return "\n".join(self.lines)
    
    def __repr__(self):
        return "\n".join(self.lines)

    @classmethod
    def fromFile(cls,src,t = False, fix = True):
        artFile = open(src,"r")
        artStr = artFile.read()
        artLines = artStr.split("\n")
        return cls(*artLines,t=t,fix=fix)

    @classmethod
    def fromString(cls,txt,t = False, fix = True):
        lines = txt.split("\n")
        return cls(*lines,t=t,fix=fix)