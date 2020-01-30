class SquareCircle(Scene):
    class Draw:
        r = 0.5
        c = lambda r: Circle(radius=r)
        s = lambda r: Square(p1=(0,0), p2=(r,1))

SquareCircle()
