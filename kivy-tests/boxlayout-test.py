from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        label1 = Label(text='Oh', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.2, 'center_y': 0.5})
        label2 = Label(text='Hello', size_hint=(0.4, 0.7), pos_hint={'center_x': 0.4, 'center_y': 0.1})
        label3 = Label(text='There', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.6, 'center_y': 0.5})

        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)

        return layout
    
if __name__ == '__main__':
    MyApp().run()
