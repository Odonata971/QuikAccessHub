from kernel import launch_applications
from customtkinter import *
import ui_config_page as config


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x450")
        self.title("QuikAccessHub")

        self.grid_rowconfigure(3, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.title = TitleFrame(master=self, fg_color="#FFFFFF")
        self.title.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        self.templates = TemplatesFrame(master=self, fg_color="#FFFFFF")
        self.templates.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

        self.configure_templates = ConfigureTemplates(master=self, fg_color="#FFFFFF")
        self.configure_templates.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")


class TemplatesFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(6, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        templates = ["Work", "Anime", "Games", "Dev", "Music"]
        # add widgets onto the frame, for example:
        self.label = CTkLabel(self, text="Choose a template", font=CTkFont(family="Bahnschrift", size=20),
                              text_color="#353535")

        self.template_01 = CTkButton(self, text=templates[0], command=lambda: launch_applications(templates[0]),
                                     font=CTkFont(family="Bahnschrift", size=15))
        self.template_02 = CTkButton(self, text=templates[1], command=lambda: launch_applications(templates[1]),
                                     font=CTkFont(family="Bahnschrift", size=15))
        self.template_03 = CTkButton(self, text=templates[2], command=lambda: launch_applications(templates[2]),
                                     font=CTkFont(family="Bahnschrift", size=15))
        self.template_04 = CTkButton(self, text=templates[3], command=lambda: launch_applications(templates[3]),
                                     font=CTkFont(family="Bahnschrift", size=15))
        self.template_05 = CTkButton(self, text=templates[4], command=lambda: launch_applications(templates[4]),
                                     font=CTkFont(family="Bahnschrift", size=15))

        self.label.grid(row=0, column=0, padx=20, pady=15)
        self.template_01.grid(row=1, column=0, padx=20, pady=5)
        self.template_02.grid(row=2, column=0, padx=20, pady=5)
        self.template_03.grid(row=3, column=0, padx=20, pady=5)
        self.template_04.grid(row=4, column=0, padx=20, pady=5)
        self.template_05.grid(row=5, column=0, padx=20, pady=5)


class TitleFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.title = CTkLabel(self, text="QuikAccessHub", font=CTkFont(family="Bahnschrift", size=40, weight="bold"),
                              text_color="#353535")
        self.title.grid(row=0, column=0, padx=5, pady=5)


class ConfigureTemplates(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)  # configure grid syst:em
        self.grid_columnconfigure(2, weight=1)
        self.configure_templates = CTkButton(self, text="Configure Templates", command=config.config_page,
                                             font=CTkFont(family="Bahnschrift", size=15))
        self.help = CTkButton(self, text="Help", command=print("help"), font=CTkFont(family="Bahnschrift", size=15))
        self.configure_templates.grid(row=0, column=0, padx=70, pady=10)
        self.help.grid(row=0, column=1, padx=45, pady=10)


app = App()
app.configure(fg_color="#D9D9D9")
app.mainloop()
