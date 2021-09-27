import tkinter as tk
import json


def main():
    root = tk.Tk()
    app = Menu(master=root)
    app.master.title("My little Fischle")
    root.geometry("400x200+800+200")
    app.master.rowconfigure(0, minsize=100, weight=1)
    app.master.columnconfigure(0, minsize=100, weight=1)
    app.mainloop()


class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        Game(self.master)
        #self.layout()
        self.grid()

    '''def layout(self):
        btn_start = tk.Button(self, text="START", command=self.start)
        btn_deck = tk.Button(self, text="DECK", command=self.deck)
        btn_start.grid(row=0, column=0, sticky="nsew", pady=10)
        btn_deck.grid(row=1, column=0, sticky="nsew", pady=10)'''

    def start(self):
        pass

    def deck(self):
        pass


class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master, relief="sunken", borderwidth=3)
        self.master = master
        self.layout()
        self.grid(row=0, column=0)

    def layout(self):
        print("Tworze layout dla gry")
        lbl_front = tk.Label(self.master, width=20, text="Tu ma być FRONT")
        ent_back = tk.Entry(self.master, width=20, text="Tu ma być BACK")
        lbl_front.grid(row=0, column=0, sticky="nsew", pady=10)
        ent_back.grid(row=1, column=0, sticky="nsew", pady=10)


class Options(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=1)

    def layout(self):
        print("Okienko?")
        btn_load = tk.Button(self.master, text="LOAD")
        btn_load.grid()


class Deck:
    def __init__(self, name):
        self.deck = {}
        self.name = name

    def load(self):
        with open(f"{self.name}.json", "r") as file:
            self.deck = json.load(file)

    def save(self):
        with open(f"{self.name}.json", "w") as file:
            json.dump(self.deck, file)

    def show(self):
        print(self.deck)


if __name__ == '__main__':
    main()
