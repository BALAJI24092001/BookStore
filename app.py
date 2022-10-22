from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Book_Store(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #add widgets to window

        self.img = Image(source='images/books.png')
        self.lab = Label(
                        text="Enter book name",
                        font_size = 16, 
                        color="#00FFCE"
                        )
        self.inp = TextInput(
                        multiline=False,
                        padding_y = (20, 20),
                        size_hint = (1, 0.5),
                        padding_x = (5, 5)
                        )
        self.but = Button(
                        text="SEARCH",
                        size_hint = (1, 0.5),
                        bold = True,
                        background_color = "#00FFCE"
                        )
        self.but.bind(on_press=self.callback)


        self.window.add_widget(self.img)
        self.window.add_widget(self.lab)
        self.window.add_widget(self.inp)
        self.window.add_widget(self.but)

        return self.window

    def click(self, ins):
        text = self.inp.text;
        pass

    def callback(self, instance):
        self.lab.text = "Hello " + self.inp.text + "!"



if __name__ == "__main__":
    Book_Store().run()
