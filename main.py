
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.expression = ""

        root = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=8
        )

        self.display = TextInput(
            text="0",
            readonly=True,
            halign="right",
            font_size=36,
            size_hint=(1, 0.25)
        )
        root.add_widget(self.display)

        grid = GridLayout(
            cols=4,
            spacing=6
        )

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for symbol in buttons:
            button = Button(
                text=symbol,
                font_size=26
            )
            button.bind(
                on_press=self.button_pressed
            )
            grid.add_widget(button)

        root.add_widget(grid)
        return root

    def button_pressed(self, button):
        symbol = button.text

        if symbol == "C":
            self.expression = ""
            self.display.text = "0"

        elif symbol == "=":
            try:
                allowed = "0123456789+-*/. "
                if not self.expression:
                    return
                if any(c not in allowed for c in self.expression):
                    return

                result = eval(self.expression)
                self.expression = str(result)
                self.display.text = self.expression

            except Exception:
                self.expression = ""
                self.display.text = "Error"

        else:
            self.expression += symbol
            self.display.text = self.expression


CalculatorApp().run()
