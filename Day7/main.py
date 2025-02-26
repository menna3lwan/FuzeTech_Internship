import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def calculate_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class ColoredPoint(Point):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color

    def __str__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"

if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(6, 8)

    print("Point 1:", p1)
    print("Point 2:", p2)

    print("Distance of P1 from origin:", p1.distance_to_origin())
    print("Distance between P1 and P2:", p1.calculate_distance(p2))

    p1.move(2, 3)
    print("P1 after moving:", p1)

    p3 = p1 + p2
    print("P3 (P1 + P2):", p3)

    print("Are P1 and P2 equal?", p1 == p2)

    cp = ColoredPoint(5, 7, "red")
    print("Colored Point:", cp)
