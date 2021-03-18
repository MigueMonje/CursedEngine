"""
    2D Vector.
"""
class Vector2:
    x,y = None,None
    
    def __init__(self,x,y):
        self.x, self.y = x, y
    
    def __add__(self,other):
        if type(other) == Vector2:
            return Vector2(self.x + other.x, self.y + other.y)
        if type(other) in (int,float):
            return Vector2(self.x + other, self.y + other)
    
    def __sub__(self,other):
        if type(other) == Vector2:
            return Vector2(self.x - other.x, self.y - other.y)
        if type(other) in (int,float):
            return Vector2(self.x - other, self.y - other)
    def between(self,a,b):
        if not Vector2 in (type(a),type(b)):
            TypeError("Arguments must be Vector2.")
        return (self.x > a.x) and (self.y > a.y) and (self.x < b.x) and (self.y < b.y)

    def __neg__(self):
        return Vector2(-self.x,-self.y)
        
    def __mul__(self,other):
        if type(other) == Vector2:
            return self.x * other.x + self.y * other.y
        if type(other) in (int,float):
            return Vector2(self.x * other, self.y * other)
        
    def __str__(self):
        return f"Vector2({self.x},{self.y})"

    def __repr__(self):
        return f"Vector2({self.x},{self.y})"