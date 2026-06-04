
# IMPORT STATEMENTS

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage

import pokebase as pb

# START SCREEN
class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.input_box = TextInput(
            hint_text="Enter Poke Name: "
        )
        
        search_button = Button(
            text="Find My Pokemon"
        )
        search_button.bind(on_press=self.search)

        layout.add_widget(self.input_box)
        layout.add_widget(search_button)
        self.add_widget(layout)

    def search(self, instance):
        
        pokemon = pb.pokemon(self.input_box.text.lower())

        pokemon_screen = self.manager.get_screen("pokemon")
        pokemon_screen.sprite.source = pokemon.sprites.front_default

        self.manager.current = "pokemon"


# POKEMON AVATAR SCREEN
class PokemonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(
            orientation="vertical",

            size_hint=(0.9, 0.9),
            pos_hint={"center_x": 0.5, "center_y": 0.6}
        )

        back_button = Button(
            text="Go Back",
            size_hint=(0.3, 0.4),
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )

        back_button.bind(on_press=self.go_back)

# SPRITE STUFF

        self.sprite = AsyncImage()
        layout.add_widget(self.sprite)

        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        
        self.manager.current = "search"


# APP BUILD
class PokeApp(App):
    def build(self):

        sm = ScreenManager()

        sm.add_widget(SearchScreen(name="search"))
        sm.add_widget(PokemonScreen(name="pokemon"))

        return sm

if __name__ == '__main__':
    PokeApp().run()