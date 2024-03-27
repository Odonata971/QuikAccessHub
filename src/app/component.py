from customtkinter import CTkFrame, CTkLabel, CTkFont


class TitleFrame(CTkFrame):
    def __init__(self, master, title: str, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.title = CTkLabel(self, text=title, font=CTkFont(family="Bahnschrift", size=40, weight="bold"),
                              text_color="#353535")
        self.title.grid(row=0, column=0, padx=5, pady=5)
