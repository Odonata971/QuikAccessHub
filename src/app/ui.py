from kernel import launch_applications
from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x450")
        self.title("QuikAccessHub")
        templates = ["Work", "Anime", "Games", "Dev", "Music"]

        self.titre = CTkLabel(self, text="QuikAccessHub", font=("Arial", 30))
        self.titre.pack(padx=5, pady=5)

        self.parameters = CTkButton(self,text="parameters")
        self.parameters.pack(padx=5, pady=5)
        self.template_01 = CTkButton(self, text=templates[0], command=lambda: launch_applications(templates[0]))
        self.template_02 = CTkButton(self, text=templates[1], command=lambda: launch_applications(templates[1]))
        self.template_03 = CTkButton(self, text=templates[2], command=lambda: launch_applications(templates[2]))
        self.template_04 = CTkButton(self, text=templates[3], command=lambda: launch_applications(templates[3]))
        self.template_05 = CTkButton(self, text=templates[4], command=lambda: launch_applications(templates[4]))
        self.template_01.pack(padx=5, pady=5)
        self.template_02.pack(padx=5, pady=5)
        self.template_03.pack(padx=5, pady=5)
        self.template_04.pack(padx=5, pady=5)
        self.template_05.pack(padx=5, pady=5)


app = App()
app.mainloop()
