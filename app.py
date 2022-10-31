from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import sqlite3



class Book_Store(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.7, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.img = Image(source='images/books.png')
        self.lab = Label(
                        text="Enter book name",
                        font_size = 16, 
                        color="#00FFCE"
                        )
        self.inp = TextInput(
                        multiline=False,
                        padding_y = (10, 10),
                        size_hint = (1, 0.5),
                        padding_x = (5, 5)
                        )
        self.but = Button(
                        text="ADD",
                        size_hint = (1, 0.5),
                        bold = True,
                        background_color = "#00FFCE"
                        )
        self.but.bind(on_press=self.callback)
        self.inpr = TextInput(padding_y = (20, 20), padding=15)
        self.butStop = Button(
                        text="PRINT",
                        size_hint=(1, 0.5),
                        bold=True,
                        background_color="#00FFCE"
                )
        self.butStop.bind(on_press= self.clear)

        self.window.add_widget(self.img)
        self.window.add_widget(self.lab)
        self.window.add_widget(self.inp)
        self.window.add_widget(self.but)
        self.window.add_widget(self.inpr)
        self.window.add_widget(self.butStop)

        return self.window

    def click(self, instance):
        self.text = self.inp.text;

    def callback(self, instance):
        con = sqlite3.connect("books.db")
        cur = con.cursor()

        b_name = self.inp.text
        try:

            query = "SELECT * FROM BOOKS WHERE book_name='"+b_name+"'"
            cur.execute(query)
            lst = list(cur.fetchall()[0])
        except:
            return

        isbn = lst[0]
        book_name = lst[1]
        author_name = lst[2]
        publisher = lst[3]
        price = lst[4]

        string = self.inpr.text + "\n" + "ISBN : " + str(isbn).ljust(15) + book_name[:8].ljust(10) + " "*5 + author_name[:10].ljust(10) + " "*5 + str(price).rjust(10)
        self.inpr.text = string


    def clear(self):
        self.inpr.text = ""
if __name__ == "__main__":
    Book_Store().run()
