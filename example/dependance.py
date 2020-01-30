from nanim import Scene, Square

# %%
class A(Scene):
    class Draw:
        a = 1
        b = lambda a: a*2
A(a=5).b # = 10

# %%

class Test(Square):
    class Draw:
        a = 0
        default__p1 = lambda a: (a, a)
        default__p2 = lambda default__p1: (default__p1[0]+1, default__p1[1]+1)

Test(a=-1) # A square from left top corner to center
