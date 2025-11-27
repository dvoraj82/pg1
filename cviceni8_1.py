class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return "Vektor({self.x}, {self.y})"
    
if __name__ == "__main__":
    v1 = Vector(3, 4)
    print(v1)
    v2 = Vector(5, 6)
    print(v2)

    v3 = v1 + v2
    print(v3)

    v4 = v1 * 3
    print(v4)

    

