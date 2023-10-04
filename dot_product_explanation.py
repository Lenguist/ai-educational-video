from manim import *

# Scene 1: Introduction
class Intro(Scene):
    def construct(self):
        # Narration: "Hello and welcome to today's lesson on the Dot Product! ..."
        title = Text("Understanding the Dot Product")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

# Scene 2: Definition
class Definition(Scene):
    def construct(self):
        # Narration: "The dot product is an operation that takes two vectors and returns a scalar. ..."
        definition = Text("Dot Product: An operation that takes two vectors and returns a scalar.")
        self.play(Write(definition))
        self.wait(2)
        self.play(FadeOut(definition))

# Scene 3: Mathematical Formula
class Formula(Scene):
    def construct(self):
        # Narration: "The mathematical formula for the dot product between vectors \( \vec{A} \) and \( \vec{B} \) is given by \( \vec{A} \cdot \vec{B} = A_x \times B_x + A_y \times B_y \) in 2D."
        formula = MathTex("\\vec{A} \\cdot \\vec{B} = A_x \\times B_x + A_y \\times B_y")
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula))

# Scene 4: Geometric Interpretation
class GeometricInterpretation(Scene):
    def construct(self):
        # Narration: "One way to understand the dot product is geometrically. ..."
        vec_A = Arrow(ORIGIN, [1, 2, 0], color=BLUE)
        vec_B = Arrow(ORIGIN, [2, 1, 0], color=GREEN)

        self.play(Create(vec_A), Create(vec_B))
        self.wait(2)
        self.play(FadeOut(vec_A), FadeOut(vec_B))

# Scene 5: Conclusion
class Conclusion(Scene):
    def construct(self):
        # Narration: "So, the dot product helps us understand the relationship between two vectors ..."
        conclusion = Text("The dot product tells us about the relationship between two vectors.")
        self.play(Write(conclusion))
        self.wait(2)