import tkinter as tk
x= 0
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.speed = tk.Button(self)
        self.speed["text"] = "Aumentar Número"
        self.speed["command"] = self.say_a
        self.speed.pack(side="top")

        self.speed = tk.Button(self)
        self.speed["text"] = "Diminuir Número"
        self.speed["command"] = self.say_d
        self.speed.pack(side="top")


    def say_a(self):
        global x
        x += 10
        print(x)
    def say_d(self):
        global x
        x -=10
        print(x)
root = tk.Tk()
app = Application(master=root)
app.mainloop()