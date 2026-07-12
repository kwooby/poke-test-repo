# IMPORT STATEMENTS

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from pprint import pprint

import pokebase as pb
import requests

# GET EVOLUTION LINE
def get_evolution_line(pokemon_name):
    species = pb.pokemon_species(pokemon_name)
    evo_chain = species.evolution_chain.chain

    evolutions = []

    def traverse(chain):
        curr_name = chain.species.name.title()

        for evo in chain.evolves_to:
            details = evo.evolution_details[0] if evo.evolution_details else None

            method = getattr(details.trigger, "name", "unknown") if details else "unknown"
            level = getattr(details, "min_level", None)

            evolutions.append({
                "from": curr_name,
                "to": evo.species.name.title(),
                "method": method,
                "level": getattr(details, "min_level", ""),
                "friendship": getattr(details, "min_happiness", None)
            })
            traverse(evo)
            
    traverse(evo_chain)
    return evolutions

# START-SEARCH SCREEN
class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.pokemon_cache = {}
        self.sprite_cache = {}

        layout = FloatLayout()

        self.input_box = TextInput(
            hint_text="Enter Poke Name: ",
            size_hint=(0.3, 0.06),
            pos_hint={"center_x":0.5,"center_y": 0.6},
            multiline=False,
        )

        search_button = Button(
            text="Find That Pokemon!",
            size_hint=(0.4, 0.1),
            pos_hint = {"center_x" : 0.5 , "center_y":0.46}
        )
        search_button.bind(on_press=self.search)
        self.input_box.bind(on_text_validate=self.search)

        layout.add_widget(self.input_box)
        layout.add_widget(search_button)

        self.add_widget(layout)
    
    def get_pokemon(self, name):
        
        if name in self.pokemon_cache:
            return self.pokemon_cache[name]
        
        pokemon = pb.pokemon(name)

        self.pokemon_cache[name] = pokemon

        return pokemon
    
    def build_evolution_text(self, pokemon): 
        evo_list = get_evolution_line(pokemon.species.name)
        evo_text = ""

        for evo in evo_list:
            if evo["friendship"]:
                evo_text += f"{evo["from"]} -(Friendship {evo["friendship"]})-> {evo["to"]}\n"
            elif evo["level"]:
                evo_text += f"{evo["from"]} -(Lv. {evo["level"]})-> {evo["to"]}\n"
            else:
                evo_text += f"{evo["from"]} -({evo["method"]})-> {evo["to"]}\n"
        
        return evo_text
        
    def find_sprite(self, pokemon):
        
        pokemon = self.get_pokemon(pokemon)
        pokemon_screen = self.manager.get_screen("pokemon")
        
        sprite_url = pokemon.sprites.front_default
        shiny_sprite_url = pokemon.sprites.front_shiny

        pokemon_screen.sprite.source = sprite_url
        pokemon_screen.shiny_sprite.source = shiny_sprite_url

        return sprite_url

    def search(self, instance):
    
        pokemon_name = self.input_box.text.strip().lower()
        pokemon_screen = self.manager.get_screen("pokemon")

        try:
            pokemon = self.get_pokemon(pokemon_name)

        except Exception:
                # POKEMON LOOKUP FAILURE
                error_screen = self.manager.get_screen("error")
                error_screen.error_label.text = (f"{self.input_box.text} has not been discovered yet!")
                self.manager.current = "error"
                return

        #sprite_url = pokemon.sprites.front_default
        #shiny_sprite_url = pokemon.sprites.front_shiny

        #if sprite_url and shiny_sprite_url:
        #    pokemon_screen.sprite.source = sprite_url
        #    pokemon_screen.shiny_sprite.source = shiny_sprite_url
        #else:
        #    pokemon_screen.sprite.source = ""
        #    pokemon_screen.shiny_sprite.source= ""

        stat_text = f"Base Stats for {pokemon.name.title()} \n\n"
        bst = 0 
        poketype = []

        for t in pokemon.types:
            poketype.append(t.type.name.upper())

        for stat in pokemon.stats:
            
            stat_name = stat.stat.name.replace("-", " ").title()
            stat_text += (
                f"{stat_name}: "
                f"{stat.base_stat}\n"
                )

            bst += stat.base_stat 

        bst_text = f"Base Stat Total: {bst}"
        poketype_text = " / ".join(poketype)
        normal_abilities = []
        hidden_abilities = []

        for ability in pokemon.abilities:
            if ability.is_hidden:
                hidden_abilities.append(ability.ability.name.upper())
            else:
                normal_abilities.append(ability.ability.name.upper())

            if normal_abilities:
                abilities_text ="Abilities:\n"
                abilities_text += "\n".join(normal_abilities)

            if hidden_abilities:
                abilities_text+="\n\nHidden Abilities:\n"
                abilities_text+="\n".join(hidden_abilities)
            else:
                pass

        pokemon_screen.evos.text = self.build_evolution_text(pokemon)
        pokemon_screen.stats.text = stat_text
        pokemon_screen.bst.text = bst_text
        pokemon_screen.type.text = poketype_text
        pokemon_screen.abilities.text = abilities_text

        self.manager.current = "pokemon"


# POKEMON SCREEN
class PokemonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # STAT INFO
        self.stats = Label(
            text="PokeStats",
            pos_hint={"center_x": 0.4, "center_y": 0.4},
        )
        
        self.bst = Label(
            text="BaseStatTotal",
            pos_hint={"center_x": 0.39, "center_y": 0.25}
        )
        
        self.type = Label(
            text="PokeType",
            pos_hint={"center_x":0.5, "center_y":0.6},
            size_hint=(0.4, 0.12)
        )

        self.evos = Label(
            text="Pokemon Evolution Chain",
            pos_hint={"center_x":0.5,"center_y":0.8}
        )

        self.abilities = Label(
            text="PokeAbilities",
            pos_hint={"center_x":0.6, "center_y":0.4}
        )

        # SPRITES
        self.sprite = AsyncImage(
            size_hint=(None,None),
            pos_hint={"center_x": 0.45, "center_y": 0.7}
        )
        self.shiny_sprite = AsyncImage(
            size_hint=(None, None),
            pos_hint={"center_x":0.55, "center_y":0.7}
        )
        
        back_button = Button(
            text="Go Back",
            size_hint=(0.2, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.1}
        )

        back_button.bind(on_press=self.go_back)
        
        layout.add_widget(self.sprite)
        layout.add_widget(self.shiny_sprite)
        layout.add_widget(self.stats)
        layout.add_widget(self.abilities)
        layout.add_widget(self.type)
        layout.add_widget(self.bst)
        layout.add_widget(self.evos)

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