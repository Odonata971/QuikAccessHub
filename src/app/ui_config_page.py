from os.path import basename
from tkinter import PhotoImage
from customtkinter import *
from template_service import *
from os import path


class ConfigurationFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(6, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)


class TitleFrame(CTkFrame):
    def __init__(self, master, title: str, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.title = CTkLabel(self, text=title, font=CTkFont(family="Bahnschrift", size=40, weight="bold"),
                              text_color="#353535")
        self.title.grid(row=0, column=0, padx=5, pady=5)


class App(CTkFrame):
    def __init__(self, master, app_path: str, tab_url=None, **kwargs):
        super().__init__(master, **kwargs)
        self.tab_url = tab_url
        self.app_path = app_path
        self.app_path_SV: StringVar = StringVar()

        self.grid_columnconfigure(0, weight=1)  # configure grid system

        self.label_path_app = CTkLabel(self, text=get_application_name(app_path), fg_color="transparent",
                                       text_color="#000")
        self.entry_path_app = CTkEntry(self, placeholder_text="Chemin vers l'executable du navigateur",
                                       text_color="#FFFFFF", textvariable=self.app_path_SV)
        self.explorer_button = CTkButton(self, text="Explorer", command=lambda: self.open_explorer())
        self.entry_path_app.insert(0, app_path)

        if not path.exists(app_path):  # If the path doesn't exist we change the color of the text
            self.label_path_app.configure(text_color="#FF0000")
            self.entry_path_app.configure(text_color="#FF0000")
        self.app_path_SV.trace("w", self.update())

        self.label_path_app.grid(row=1, column=0, padx=(10, 2), sticky="w")
        self.entry_path_app.grid(row=2, column=0, padx=10, pady=(0, 20), sticky="ew")
        self.explorer_button.grid(row=2, column=1, padx=10, pady=(0, 20), sticky="ew")

        if tab_url is not None:
            self.entry_url: list[CTkEntry] = []
            self.label_url: list[CTkLabel] = []

            for i in range(len(tab_url)):
                self.label_url.append(CTkLabel(self, text="Url", fg_color="transparent", text_color="#000"))
                self.entry_url.append(CTkEntry(self, text_color="#FFFFFF"))

                self.entry_url[i].insert(0, tab_url[i])

                self.label_url[i].grid(row=2 * i + 3, column=0, padx=10, sticky="w")
                bottom_pading = 0
                if i == len(tab_url) - 1:  # If it's the last url we add a bottom padding
                    bottom_pading = 10
                self.entry_url[i].grid(row=2 * i + 4, column=0, padx=10, pady=(0, bottom_pading), sticky="ew")

            # TODO Add a button to add a new url

    def get_data(self) -> dict:
        data = {"path": self.entry_path_app.get()}
        if self.tab_url is not None:
            data["urls"] = [url.get() for url in self.entry_url]
        return data

    def open_explorer(self):
        """
        Open the explorer to choose a browser executable
        """
        file_path = filedialog.askopenfilename(initialdir="/", title="Selectionner un executable",
                                               filetypes=(("executables", "*.exe"), ("all files", "*.*")))
        if file_path != "":
            self.entry_path_app.delete(0, END)
            self.entry_path_app.insert(0, file_path)
            if not path.exists(file_path):
                self.label_path_app.configure(text_color="#FF0000")
                self.entry_path_app.configure(text_color="#FF0000")
            else:
                self.label_path_app.configure(text_color="#000")
                self.entry_path_app.configure(text_color="#FFFFFF")

    def __str__(self):
        if self.entry_path_app.get() == "":
            return "App (empty)"
        return "App " + get_application_name(self.entry_path_app.get())

    def update(self):
        self.app_path = self.entry_path_app.get()
        self.label_path_app.configure(text=get_application_name(self.app_path))
        if not path.exists(self.app_path):
            self.label_path_app.configure(text_color="#FF0000")
            self.entry_path_app.configure(text_color="#FF0000")
        else:
            self.label_path_app.configure(text_color="#000")
            self.entry_path_app.configure(text_color="#FFFFFF")


def add_app(scroll: CTkScrollableFrame, app: list[App | None]):
    app.insert(0, App(master=scroll, app_path="", fg_color="#FFFFFF"))
    for i in range(len(app)):
        app[i].grid(row=i + 1, column=0, padx=20, pady=10, sticky="new")
    pass


def show_template(template_name: str):
    print("Configuring template : " + template_name)
    # Get the template data
    template_data: list[dict] = get_info_template(template_name)
    app: list[App] = []

    window = CTk()
    window.configure(fg_color="#D9D9D9")
    window.title("QuikAccessHub - " + template_name)
    window.geometry("700x500")
    window.resizable(False, False)
    window.grid_columnconfigure(0, weight=1)  # configure grid system
    window.grid_rowconfigure(3, weight=1)

    title = TitleFrame(master=window, fg_color="#FFFFFF", title="Config of " + template_name)
    scroll = CTkScrollableFrame(master=window, fg_color="transparent")
    scroll.grid_columnconfigure(0, weight=1)
    save_button = CTkButton(master=window, text="Sauvegarder",
                            command=lambda: save_template(template_name, app, window))
    add_app_button = CTkButton(master=window, text="Ajouter une application", command=lambda: add_app(scroll, app))

    title.grid(row=0, column=0, padx=20, pady=10, sticky="new")
    save_button.grid(row=1, column=0, padx=20, pady=10, sticky="new")
    add_app_button.grid(row=2, column=0, padx=20, pady=10, sticky="new")
    scroll.grid(row=3, column=0, padx=20, sticky="snew")

    for i in range(len(template_data)):
        if "urls" in template_data[i]:
            app.append(App(master=scroll, app_path=template_data[i]["path"], tab_url=template_data[i]["urls"],
                           fg_color="#FFFFFF"))
        else:
            app.append(App(master=scroll, app_path=template_data[i]["path"], fg_color="#FFFFFF"))

        app[i].grid(row=i, column=0, padx=20, pady=10, sticky="new")



    window.mainloop()


def config_page():
    window = CTk()
    window.configure(fg_color="#D9D9D9")
    window.title("QuikAccessHub - Config Page")
    window.title = TitleFrame(master=window, fg_color="#FFFFFF", title="Config Page")
    window.title.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

    window.geometry("400x300")
    window.resizable(False, False)

    window.grid_columnconfigure(0, weight=1)  # configure grid system

    # Get the list of templates
    templates = get_template_list().keys()
    templates_button = []  # list of buttons for each template

    if len(templates) == 0:
        label = CTkLabel(window, text="No template found", font=CTkFont(family="Bahnschrift", size=20),
                         text_color="#353535")
        label.grid(row=1, column=0, padx=20, pady=15)

    # Create a button for each template
    for template in templates:
        # To avoid the problem of the button always taking the last value of template,
        # we use a lambda function with a default argument
        templates_button.append(CTkButton(window, text=template,
                                          command=lambda template_used=template: show_template(template_used),
                                          font=CTkFont(family="Bahnschrift", size=15)))

    # Grid the buttons
    for i in range(len(templates_button)):
        templates_button[i].grid(row=i + 1, column=0, padx=20, pady=10, sticky="nsew")

    window.mainloop()


def get_application_name(executable_path: str) -> str:
    return os.path.splitext(os.path.basename(executable_path))[0]



def save_template(template_name: str, app: list[App | None], window: CTk):
    print("Saving template : " + template_name)
    new_template_data = [i.get_data() for i in app if i is not None]
    update_template(template_name, new_template_data)

    window.destroy()  # Close the window
