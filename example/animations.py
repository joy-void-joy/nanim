class ThreeCircles(Scene):
    class Circle(Circle):
        default__r = 0.2
        default__color = "white"
    three_circles = Circle().times(3)

ThreeCircles()
