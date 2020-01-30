from nanim.Scene import Scene

class Square(Scene):
    def draw(self):
        def tween(i):
            return int((i+1)*50)
        out = np.full((100, 100), None)
        out[tween(self.Draw.p1[0]):tween(self.Draw.p2[0]), tween(self.Draw.p1[1]):tween(self.Draw.p2[1])] = 255
        return out

    class Draw:
        p1 = (-1, -1)
        p2 = (1, 1)
