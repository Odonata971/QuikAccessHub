from kernel import launch_applications
from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.title("QuikAccessHub")
        self.button = CTkButton(self, text="my button", command=launch_applications)
        self.button.pack(padx=20, pady=20)


app = App()
app.mainloop()
