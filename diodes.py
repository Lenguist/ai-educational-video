from manim import *

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("The Mathematical Magic of Diodes", font_size=40)
        self.play(Write(title))
        self.wait(1)
        
        # Fade out title
        self.play(FadeOut(title))
        self.wait(1)

        # Simple electronic circuit
        resistor = Rectangle(height=0.2, width=0.6, color=WHITE)
        resistor_label = Text("R", font_size=30).next_to(resistor, DOWN, 0.1)
        diode = Arrow(start=LEFT * 0.3, end=RIGHT * 0.3, color=WHITE, buff=0)
        diode_label = Text("D", font_size=30).next_to(diode, UP, 0.1)
        wire = Line(start=LEFT * 1.5, end=RIGHT * 1.5, color=WHITE)

        circuit_group = VGroup(resistor, diode, wire).arrange(RIGHT, buff=1)
        label_group = VGroup(resistor_label, diode_label)

        self.play(FadeIn(circuit_group), FadeIn(label_group))
        self.wait(1)

        # Narration
        narration = Text(
            "Hello everyone! Today, we're diving into the\n"
            "fascinating world of diodes. These tiny electronic\n"
            "components may seem simple, but there's a lot of\n"
            "mathematical beauty and complex physics behind how\n"
            "they work.",
            font_size=30
        ).to_edge(DOWN)
        
        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(circuit_group), FadeOut(label_group), FadeOut(narration))

from manim import *

class BasicIdeaScene(Scene):
    def construct(self):
        # Diode Symbol
        arrow = Arrow(start=LEFT * 0.3, end=RIGHT * 0.3, color=WHITE, buff=0)
        line = Line(start=LEFT * 0.3, end=RIGHT * 0.3, color=WHITE)
        diode_symbol = VGroup(line, arrow).arrange(RIGHT, buff=0.1)
        
        # Circuit Representation
        wire1 = Line(start=LEFT * 1.5, end=RIGHT * 1.5, color=WHITE)
        wire2 = Line(start=LEFT * 1.5, end=RIGHT * 1.5, color=WHITE)
        diode_circuit = Arrow(start=LEFT * 0.3, end=RIGHT * 0.3, color=WHITE, buff=0)
        
        circuit_group = VGroup(wire1, diode_circuit, wire2).arrange(RIGHT, buff=0.5)

        # Grouping and positioning
        all_diode_rep = VGroup(diode_symbol, circuit_group).arrange(DOWN, buff=1)
        self.play(FadeIn(all_diode_rep))
        self.wait(1)
        
        # Narration
        narration = Text(
            "A diode is essentially an electronic one-way street.\n"
            "It allows electric current to flow in one direction\n"
            "but blocks it in the opposite direction.",
            font_size=30
        ).to_edge(DOWN)
        
        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(all_diode_rep), FadeOut(narration))

from manim import *

class SemiconductorsScene(Scene):
    def construct(self):
        # Silicon Atom Structure
        silicon_core = Dot(radius=0.2, color=YELLOW)
        electron_orbit = Circle(radius=0.8, color=WHITE).next_to(silicon_core, UP, 0)
        electrons = [Dot(radius=0.1, color=BLUE).move_to(electron_orbit.point_at_angle(360 * i / 4)) for i in range(4)]

        silicon_atom = VGroup(silicon_core, electron_orbit, *electrons)

        # N-type and P-type semiconductors
        n_type_label = Text("N-type", font_size=30).next_to(silicon_atom, RIGHT, buff=2)
        p_type_label = Text("P-type", font_size=30).next_to(n_type_label, RIGHT, buff=2)

        n_type_icon = Rectangle(height=0.8, width=0.8, color=WHITE).next_to(n_type_label, DOWN, buff=0.2)
        n_type_extra = Dot(radius=0.1, color=RED).next_to(n_type_icon, UP, buff=0.1)

        p_type_icon = Rectangle(height=0.8, width=0.8, color=WHITE).next_to(p_type_label, DOWN, buff=0.2)
        p_type_hole = Dot(radius=0.1, color=WHITE).next_to(p_type_icon, UP, buff=0.1)

        n_type = VGroup(n_type_label, n_type_icon, n_type_extra)
        p_type = VGroup(p_type_label, p_type_icon, p_type_hole)

        semiconductors = VGroup(n_type, p_type).next_to(silicon_atom, RIGHT, buff=2)

        # Animation
        self.play(FadeIn(silicon_atom))
        self.play(Rotate(electron_orbit, angle=360*DEGREES, run_time=2, rate_func=linear))
        self.play(FadeIn(semiconductors))

        # Narration
        narration = Text(
            "The secret behind diodes lies in semiconductors.\n"
            "Imagine a lattice of silicon atoms, and let's introduce\n"
            "the idea of N-type and P-type semiconductors.",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(silicon_atom), FadeOut(semiconductors), FadeOut(narration))

from manim import *

class PNJunctionScene(Scene):
    def construct(self):
        # N-type semiconductor
        n_type_label = Text("N-type", font_size=30)
        n_type_icon = Rectangle(height=0.8, width=1.6, color=WHITE)
        n_type_extra = Dot(radius=0.1, color=RED).next_to(n_type_icon, UP, buff=0.1)
        
        n_type = VGroup(n_type_label, n_type_icon, n_type_extra).arrange(DOWN, buff=0.2)

        # P-type semiconductor
        p_type_label = Text("P-type", font_size=30)
        p_type_icon = Rectangle(height=0.8, width=1.6, color=WHITE)
        p_type_hole = Dot(radius=0.1, color=WHITE).next_to(p_type_icon, UP, buff=0.1)

        p_type = VGroup(p_type_label, p_type_icon, p_type_hole).arrange(DOWN, buff=0.2)

        # Positioning
        n_type.next_to(ORIGIN, LEFT, buff=0.5)
        p_type.next_to(ORIGIN, RIGHT, buff=0.5)

        # Animation
        self.play(FadeIn(n_type), FadeIn(p_type))
        self.play(n_type.animate.next_to(p_type, RIGHT, buff=0.5))

        # P-N Junction label
        pn_junction_label = Text("P-N Junction", font_size=30).to_edge(UP)

        # Narration
        narration = Text(
            "When an N-type semiconductor is brought in contact\n"
            "with a P-type, a P-N junction is formed. This is the\n"
            "heart of a diode.",
            font_size=30
        ).to_edge(DOWN)
        
        self.play(Write(pn_junction_label))
        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(n_type), FadeOut(p_type), FadeOut(pn_junction_label), FadeOut(narration))

from manim import *

class DepletionRegionScene(Scene):
    def construct(self):
        # P-N Junction
        n_type_icon = Rectangle(height=0.8, width=1.6, color=WHITE)
        p_type_icon = Rectangle(height=0.8, width=1.6, color=WHITE)
        junction = VGroup(n_type_icon, p_type_icon).arrange(RIGHT, buff=0)

        # Depletion Region
        depletion_region = Rectangle(height=0.8, width=0.2, color=RED).next_to(n_type_icon, RIGHT, buff=0)

        # Electric Field
        e_field_arrow = Arrow(start=LEFT * 0.3, end=RIGHT * 0.3, color=YELLOW).next_to(depletion_region, UP, buff=0.1)
        e_field_label = Text("E", font_size=30).next_to(e_field_arrow, UP, buff=0.1)

        # Animation
        self.play(FadeIn(junction))
        self.play(junction.animate.scale(2))  # Corrected scale method
        self.play(FadeIn(depletion_region))
        self.play(FadeIn(e_field_arrow), FadeIn(e_field_label))

        # Narration
        narration = Text(
            "At the P-N junction, a 'depletion region' forms,\n"
            "creating an electric field that opposes the flow\n"
            "of charge in one direction.",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(junction), FadeOut(depletion_region), FadeOut(e_field_arrow), FadeOut(e_field_label), FadeOut(narration))

from manim import *

class MathBehindDepletionScene(Scene):
    def construct(self):
        # Equations
        equation1 = MathTex("E(x) =", "\\frac{dV}{dx}", font_size=30)
        equation2 = MathTex("V(x) =", "-\\int E(x) dx", font_size=30)
        
        equations = VGroup(equation1, equation2).arrange(DOWN, buff=0.5)

        # Graph
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            axis_config={"color": WHITE},
        )
        
        graph = axes.plot(
            lambda x: x**2 - 1,
            color=YELLOW,
        )
        
        graph_label = axes.get_graph_label(graph, label='E(x)')

        # Animation
        self.play(Write(equations))
        self.play(FadeIn(axes), Create(graph), Write(graph_label))

        # Narration
        narration = Text(
            "Mathematically, the electric field can be described\n"
            "by these equations. Let's plot how the electric field\n"
            "varies across the junction.",
            font_size=30
        ).to_edge(DOWN)
        
        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(equations), FadeOut(axes), FadeOut(graph), FadeOut(graph_label), FadeOut(narration))

from manim import *

class ForwardBiasScene(Scene):
    def construct(self):
        # P-N Junction with Depletion Region
        n_type_icon = Rectangle(height=0.8, width=1.6, color=WHITE)
        p_type_icon = Rectangle(height=0.8, width=1.6, color=WHITE)
        depletion_region = Rectangle(height=0.8, width=0.2, color=RED).next_to(n_type_icon, RIGHT, buff=0)
        junction = VGroup(n_type_icon, p_type_icon, depletion_region).arrange(RIGHT, buff=0)

        # Voltage Arrow
        voltage_arrow = Arrow(start=DOWN * 0.5, end=UP * 0.5, color=BLUE).next_to(junction, UP, buff=0.2)
        voltage_label = Text("V", font_size=30).next_to(voltage_arrow, UP, buff=0.1)

        # Animation
        self.play(FadeIn(junction))
        self.play(FadeIn(voltage_arrow), FadeIn(voltage_label))
        self.play(depletion_region.animate.set_width(0.1))

        # Narration
        narration = Text(
            "When voltage is applied in the direction that aligns\n"
            "with the electric field of the depletion region, we get\n"
            "what's called 'Forward Bias.' The diode conducts electricity.",
            font_size=30
        ).to_edge(DOWN)
        
        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(junction), FadeOut(voltage_arrow), FadeOut(voltage_label), FadeOut(narration))

from manim import *

class ReverseBiasScene(Scene):
    def construct(self):
        # P-N Junction with Depletion Region
        n_type_icon = Rectangle(height=0.8, width=1.6, color=WHITE)
        p_type_icon = Rectangle(height=0.8, width=1.6, color=WHITE)
        depletion_region = Rectangle(height=0.8, width=0.1, color=RED).next_to(n_type_icon, RIGHT, buff=0)
        junction = VGroup(n_type_icon, p_type_icon, depletion_region).arrange(RIGHT, buff=0)

        # Voltage Arrow
        voltage_arrow = Arrow(start=UP * 0.5, end=DOWN * 0.5, color=BLUE).next_to(junction, UP, buff=0.2)
        voltage_label = Text("V", font_size=30).next_to(voltage_arrow, DOWN, buff=0.1)

        # Animation
        self.play(FadeIn(junction))
        self.play(FadeIn(voltage_arrow), FadeIn(voltage_label))
        self.play(depletion_region.animate.set_width(0.4))

        # Narration
        narration = Text(
            "But what happens if we apply voltage in the opposite direction?\n"
            "This is called 'Reverse Bias,' and the diode blocks the flow of current.",
            font_size=30
        ).to_edge(DOWN)
        
        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(junction), FadeOut(voltage_arrow), FadeOut(voltage_label), FadeOut(narration))

from manim import *

class RealWorldApplicationsScene(Scene):
    def construct(self):
        # Rectifier Circuit
        rectifier = Rectangle(height=0.6, width=1.2, color=WHITE)
        rectifier_label = Text("Rectifier", font_size=30).next_to(rectifier, DOWN, buff=0.1)
        
        # Signal Clipper Circuit
        clipper = Rectangle(height=0.6, width=1.2, color=WHITE)
        clipper_label = Text("Signal Clipper", font_size=30).next_to(clipper, DOWN, buff=0.1)

        # LED
        led_shape = Circle(radius=0.6, color=WHITE)
        led_label = Text("LED", font_size=30).next_to(led_shape, DOWN, buff=0.1)

        # Arrange the three applications
        applications = VGroup(rectifier, clipper, led_shape).arrange(RIGHT, buff=1)
        labels = VGroup(rectifier_label, clipper_label, led_label).arrange(RIGHT, buff=1)

        # Animation
        self.play(FadeIn(applications), FadeIn(labels))

        # Narration
        narration = Text(
            "Diodes are incredibly versatile. They're used in\n"
            "rectifiers, signal clippers, and even in generating\n"
            "light in LEDs!",
            font_size=30
        ).to_edge(DOWN)
        
        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(applications), FadeOut(labels), FadeOut(narration))

from manim import *

class ConclusionScene(Scene):
    def construct(self):
        # Key Points
        point1 = Text("1. One-way Electrical Flow", font_size=30)
        point2 = Text("2. P-N Junction & Depletion Region", font_size=30)
        point3 = Text("3. Forward & Reverse Bias", font_size=30)
        point4 = Text("4. Real-world Applications", font_size=30)
        
        key_points = VGroup(point1, point2, point3, point4).arrange(DOWN, buff=0.5)
        
        # Animation
        self.play(Write(point1))
        self.wait(1)
        self.play(Write(point2))
        self.wait(1)
        self.play(Write(point3))
        self.wait(1)
        self.play(Write(point4))
        self.wait(1)

        # Narration
        narration = Text(
            "So there you have it, the wonderful world of diodes—\n"
            "where physics meets mathematics to create something\n"
            "both useful and elegant.",
            font_size=30
        ).to_edge(DOWN)
        
        self.play(Write(narration))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(key_points), FadeOut(narration))
