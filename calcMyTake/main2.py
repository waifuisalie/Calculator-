from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class CalcMath:     #no need to put self here, or BoxLayout or App or some shit like that, its just a class chill
    def add(self, x, y):
        return float(x) + float(y)
    def subtract(self, x, y):
        return float(x) - float(y)
    def divide(self, x, y):
        if y == '0':
            return 'mano vsf meu'
        else:
            return float(x) / float(y)
    def multiply(self, x, y):
        return float(x) * float(y)

#I ve got a glock in my 'rari

class Box(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (500,400)
        self.math_op = CalcMath()   #need to put ()!!
        self.ids.exit.text = '[b][color=#ff0000]EXIT[/color][/b]'

    def add_fr(self, op1, op2):
        self.ids.result.text = str(self.math_op.add(op1, op2))
    def subtract_fr(self, op1, op2):
        self.ids.result.text = str(self.math_op.subtract(op1, op2))
    def divide_fr(self, op1, op2):
        self.ids.result.text = str(self.math_op.divide(op1, op2))
    def multiply_fr(self, op1, op2):
        self.ids.result.text = str(self.math_op.multiply(op1, op2))
    
    def clear(self):
        self.ids.op1.text = ''
        self.ids.op2.text = ''
        self.ids.result.text = ''

    def exit(self):
        App.get_running_app().stop()


class Calc(App):
    def build(self):
        self.title = 'Calculator'
        return Box()

Calc().run()