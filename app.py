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
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

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

    def click(self, instance):
        self.text = self.inp.text;


    def callback(self, instance):
        con = sqlite3.connect("books.db")
        cur = con.cursor()

        layout = GridLayout(cols = 1, padding = 10)

        b_name = self.inp.text
        
        query = "SELECT * FROM BOOKS WHERE book_name='"+b_name+"'"
        cur.execute(query)
        lst = list(cur.fetchall()[0])
        price = lst[4]
        quantity = int(lst[5])
        if quantity >= 0:
            lab0 = Label(text= "Price of the book : {0}".format(price) )
            lab1 = Label(text="Thank for purchasing " + b_name)
            lab2 = Label(text= "VISIT AGAIN")
            layout.add_widget(lab0)
            layout.add_widget(lab1)
            layout.add_widget(lab2)
        else:
            lab0 = Label(text = "SOLD OUT", font_size=25, color="#e30013")
            layout.add_widget(lab0)

        closeButton = Button(text = "close")

        layout.add_widget(closeButton)

        popup = Popup(title="RECEIPT",
                      content = layout,
                      size_hint = (None, None), size=(300, 200)
                      )
        popup.open()
        closeButton.bind(on_press = popup.dismiss)

if __name__ == "__main__":
    Book_Store().run()
