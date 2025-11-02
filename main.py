from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.input1 = TextInput(hint_text="Ingrese el primer número", multiline=False)
        self.input2 = TextInput(hint_text="Ingrese el segundo número", multiline=False)
        self.add_widget(self.input1)
        self.add_widget(self.input2)
        self.resultado = Label(text="Resultado: ", font_size=18)
        self.add_widget(self.resultado)
        layout_botones = BoxLayout()
        operaciones = [("Suma", self.sumar),
                       ("Resta", self.restar),
                       ("Mult.", self.multiplicar),
                       ("Div.", self.dividir)]
        for texto, funcion in operaciones:
            btn = Button(text=texto, on_press=funcion)
            layout_botones.add_widget(btn)
        self.add_widget(layout_botones)
        layout_extra = BoxLayout()
        extra_ops = [("Potencia", self.potenciar),
                     ("Raíz", self.raiz),
                     ("Complejos", self.operar_complejos)]
        for texto, funcion in extra_ops:
            btn = Button(text=texto, on_press=funcion)
            layout_extra.add_widget(btn)
        self.add_widget(layout_extra)
    def obtener_valores(self):
        try:
            a = float(self.input1.text)
            b = float(self.input2.text)
            return a, b
        except:
            self.resultado.text = "Ingrese valores numéricos válidos"
            return None, None
    def sumar(self, instance):
        a, b = self.obtener_valores()
        if a is not None:
            self.resultado.text = f"Resultado: {a + b}"
    def restar(self, instance):
        a, b = self.obtener_valores()
        if a is not None:
            self.resultado.text = f"Resultado: {a - b}"
    def multiplicar(self, instance):
        a, b = self.obtener_valores()
        if a is not None:
            self.resultado.text = f"Resultado: {a * b}"
    def dividir(self, instance):
        a, b = self.obtener_valores()
        if a is not None:
            if b != 0:
                self.resultado.text = f"Resultado: {a / b}"
            else:
                self.resultado.text = "No se puede dividir entre cero"
    def potenciar(self, instance):
        a, b = self.obtener_valores()
        if a is not None:
            self.resultado.text = f"Resultado: {a ** b}"
    def raiz(self, instance):
        a, _ = self.obtener_valores()
        if a is not None:
            if a >= 0:
                self.resultado.text = f"Resultado: {a ** 0.5}"
            else:
                self.resultado.text = "No existe raíz real de número negativo"
    def operar_complejos(self, instance):
        try:
            c1 = complex(self.input1.text)
            c2 = complex(self.input2.text)
            suma = c1 + c2
            resta = c1 - c2
            mult = c1 * c2
            self.resultado.text = f"Suma: {suma}, Resta: {resta}, Mult: {mult}"
        except:
            self.resultado.text = "Ingrese números complejos válidos (ej: 2+3j)"
class CalculadoraApp(App):
    def build(self):
        self.title = "Calculadora Kivy"
        return Calculadora()
if __name__ == "__main__":
    CalculadoraApp().run()
