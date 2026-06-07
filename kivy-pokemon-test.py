
# IMPORT STATEMENTS

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage

import pokebase as pb

# START-SEARCH SCREEN
class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        self.input_box = TextInput(
            hint_text="Enter Poke Name: ",
            size_hint=(0.6, 0.5),
            pos_hint={"center_x":0.5,"center_y": 0.6}
        )

        search_button = Button(
            text="Find That Pokemon!",
            size_hint=(0.4, 0.1),
            pos_hint = {"center_x" : 0.5 , "center_y":0.2}
        )
        search_button.bind(on_press=self.search)

        layout.add_widget(self.input_box)
        layout.add_widget(search_button)

        self.add_widget(layout)

    def search(self, instance):
        
        try:
            pokename = pb.pokemon(
                self.input_box.text.strip().lower()
            )
            sprite_url = pokename.sprites.front_default

        except Exception:
            # POKEMON LOOKUP FAILURE
            error_screen = self.manager.get_screen("error")
            error_screen.error_label.text = (
                f"{self.input_box.text} not yet discovered!"
                )
            
            self.manager.current = "error"

            return

        pokemon_screen = self.manager.get_screen("pokemon")

        if sprite_url:
            pokemon_screen.sprite.source = sprite_url
        else:
            pokemon_screen.sprite.source = " "            

        stat_text = f"Base Stats for {pokename.name.title()}: \n\n"
        for stat in pokename.stats:
            
            stat_name = stat.stat.name.replace("-", "").title()
            #bst = sum()
            stat_text += (
                f"{stat_name}: "
                f"{stat.base_stat}\n"
                )
            
        pokemon_screen.stats.text = stat_text

        self.manager.current = "pokemon"


# POKEMON SCREEN

class PokemonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.stats = Label(
            text="PokeStats",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        
        self.sprite = AsyncImage(
            size_hint=(None,None),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
            )
        
        back_button = Button(
            text="Go Back",
            size_hint=(0.4, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )

        back_button.bind(on_press=self.go_back)
        
        layout.add_widget(self.sprite)
        layout.add_widget(self.stats)

        layout.add_widget(back_button)

        self.add_widget(layout)


    def go_back(self, instance):
        self.manager.current = "search"


# ERROR SCREEN

class ErrorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.error_label = Label(
            text="Pokemon not found!"
            )
        
        back_button = Button(
            text="Go Back",
            size_hint=(0.4, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )

        back_button.bind(on_press=self.go_back)

        layout.add_widget(self.error_label)
        layout.add_widget(back_button)

        self.add_widget(layout)


    def go_back(self, instance):
        self.manager.current = "search"


# APP BUILD
class MiniDexApp(App):
    def build(self):

        sm = ScreenManager()

        sm.add_widget(SearchScreen(name="search"))
        sm.add_widget(PokemonScreen(name="pokemon"))
        sm.add_widget(ErrorScreen(name="error"))

        return sm

if __name__ == '__main__':
    MiniDexApp().run()