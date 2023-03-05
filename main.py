from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
    def __init__(self, name = 'first'):
        super().__init__(name = name)
        btn = Button(text = "Переключиться на экран")
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'left' 
                                                   
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name = 'second'):
        super().__init__(name = name)
        btn = Button(text = "Вернутся")
        btn2 = Button(text = "Далее")
        btn.on_press = self.next
        self.add_widget(btn)
        btn2.on_press = self.next2
        self.add_widget(btn2)

    def next2(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'first'
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class TriScr(Screen):
    def __init__(self, name = 'tri'):
        super().__init__(name = name)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        return sm

app = MyApp()
app.run()
