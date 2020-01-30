# This is the current porting milestone
class OpeningManimExample(Sequential):
    class First(VGroup):
        default__arrange = "down"
        title = TextMobject("This is some \\LaTeX").write()
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        ).FadeIn()
    first = First()

    class Second(Scene):
        title = lambda title: title.transform(TextMobject("That was a transform").to_corner(UP + LEFT))
        lagged = LaggedStart(*map(FadeOutAndShiftDown, basel))
    second = lambda first: Second(title=first.title)

    class Third(Scene):
        title = lambda title: title.fadeout()
        grid = NumberPlane().create()
        grid_title = TextMobject("This is a grid").scale(1.5).move_to(transform_title).fadeinfrom("down")
    third = lambda second: Third(title=second.title)

    class Fourth(Scene):
        grid_title = lambda grid_title: third.grid_title.transform(TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        ).move_to(grid_title, UL))

        deform_grid = grid.apply_function(
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                    0,
            ]),
            run_time=3,
        )
    fourth = Fourth()
