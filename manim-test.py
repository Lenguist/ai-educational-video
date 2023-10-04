from manim import *

class MovingSquare(Scene):
    def construct(self):
        square = Square()  # Create a square
        square.to_edge(LEFT)  # Move the square to the left edge

        # Create an animation where the square moves to the right edge of the screen
        self.play(square.animate.to_edge(RIGHT))
