import tkinter as tk
import json


def main():
    app = Fischl()
    app.title("My little Fischle")
    app.geometry("400x200+800+200")
    app.rowconfigure(0, minsize=100, weight=1)
    app.columnconfigure(0, minsize=100, weight=1)
    app.mainloop()


class Fischl(tk.Tk):
    def __init__(self):
        super().__init__()
        self._frame = None
        self.open_page(Menu)

    def open_page(self, frame_name):
        new_frame = frame_name(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

    def back_menu(self, master):
        frm_back = tk.Frame(master)
        btn_back = tk.Button(master, text="BACK", command=lambda: self.open_page(Menu))
        btn_back.grid(padx=10)
        frm_back.grid(row=0, column=0, sticky='nsew', )


class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.layout()

    def layout(self):
        btn_start = tk.Button(self, text="START", command=lambda: self.master.open_page(Game))
        btn_deck = tk.Button(self, text="DECK", command=lambda: self.master.open_page(Options))
        btn_start.grid(row=0, column=0, sticky="nsew", pady=10)
        btn_deck.grid(row=1, column=0, sticky="nsew", pady=10)


class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.back_menu(self)
        self.layout()

    def layout(self):
        frm_layout = tk.Frame(self)
        lbl_front = tk.Label(frm_layout, width=20, text="Tu ma być FRONT")
        ent_back = tk.Entry(frm_layout, width=20)
        lbl_front.grid(row=0, column=0, sticky="nsew", pady=10)
        ent_back.grid(row=1, column=0, sticky="nsew", pady=10)
        frm_layout.grid(row=0, column=1, sticky="nsew", pady=10)


class Options(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.back_menu(self)
        self.layout()

    def layout(self):
        btn_load = tk.Button(self, text="LOAD")
        btn_load.grid(row=0, column=1, sticky='nsew')


#=================================================================================


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
