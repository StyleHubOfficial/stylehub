from manim import *
from moviepy.editor import *

class CinematicTrailer(Scene):
    def construct(self):
        # Background Music
        bg_music = "trailer_music.mp3"  # Add your cinematic background music file
        
        # Title Animation
        title = Text("TALLENT HUB", font_size=80, font="Arial Bold").set_color(RED)
        self.play(FadeIn(title, scale=2), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), run_time=1)

        # Tagline Animation
        tagline = Text("Unleash Your Creativity\nWith Professional Designs", font_size=50)
        self.play(Write(tagline), run_time=3)
        self.wait(1)
        self.play(FadeOut(tagline), run_time=1)

        # Features
        features = [
            "🔥 High-Quality Graphic Designs",
            "🚀 Fast & Professional Services",
            "🎨 Unlimited Creativity",
            "📢 Boost Your Brand Online",
        ]
        
        for text in features:
            feature_text = Text(text, font_size=40, font="Arial").set_color(YELLOW)
            self.play(FadeIn(feature_text, shift=UP), run_time=2)
            self.wait(0.7)
            self.play(FadeOut(feature_text), run_time=1)

        # Call To Action
        cta = Text("Visit Us Now: www.tallenthub.com", font_size=45, font="Arial Bold").set_color(BLUE)
        self.play(Write(cta), run_time=2)
        self.wait(2)
        self.play(FadeOut(cta), run_time=1)

# Render command: manim -pql cinematic_trailer.py CinematicTrailer
