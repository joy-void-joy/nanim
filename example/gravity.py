# An exemple for how we can use nanim for updated animations
# TODO: How to update self
class GravityScene(Scene):
    class Cube(Scene):
        class Draw:
            all_cubes = []
            i = 0
            j = 0
            mass = 1
            pos = lambda i, j: (i, j)
            def update__pos(pos, i, j, all_cubes, mass):
                for cube in all_cubes:
                    pos += pos + (i.pos*i.mass - pos*mass).norm()
                return pos

            cube = lambda pos, mass: Square(pos=pos, size=mass)

    class Draw:
        num_cubes = 500
        default__space = lambda num_cubes: (0, 0, num_cubes, num_cubes)
        cubes = []
        cubes = lambda num_cubes: Cube(mass=1, all_cubes=[cubes]).times_cartesian(i=range(num_cubes), j = range(num_cubes))


GravityScene()
