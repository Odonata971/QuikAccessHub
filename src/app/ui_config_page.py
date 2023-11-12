from customtkinter import *


def config_page():
    # Display an error message
    window = CTk()
    window.configure(fg_color="#D9D9D9")
    window.title = TitleFrame(master=window, fg_color="#FFFFFF")
    window.title.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

    window.geometry("400x300")
    window.resizable(False, False)

    window.grid_rowconfigure(3, weight=1)  # configure grid system
    window.grid_columnconfigure(0, weight=1)

    add_config_button = CTkButton(window, text="Add a Config",font=CTkFont(family="Bahnschrift", size=15))
    add_config_button.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")


    window.mainloop()

class ConfigurationFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(6, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)


class TitleFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.title = CTkLabel(self, text="Config Page", font=CTkFont(family="Bahnschrift", size=40, weight="bold"),
                              text_color="#353535")
        self.title.grid(row=0, column=0, padx=5, pady=5)
