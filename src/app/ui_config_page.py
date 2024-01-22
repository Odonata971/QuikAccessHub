from os.path import basename
import tkinter as tk
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
        self.app_path_SV: StringVar = tk.StringVar(self, app_path)
        self.app_path_SV.trace("w", self.update_app_path_label)

        self.grid_columnconfigure(0, weight=1)  # configure grid system

        self.label_path_app = CTkLabel(self, fg_color="transparent", text_color="#000")
        self.entry_path_app = CTkEntry(self, text_color="#FFFFFF", textvariable=self.app_path_SV)
        self.explorer_button = CTkButton(self, text="Explorer", command=self.open_explorer)

        self.label_path_app.grid(row=1, column=0, padx=(10, 2), sticky="w")
        self.entry_path_app.grid(row=2, column=0, padx=10, pady=(0, 20), sticky="ew")
        self.explorer_button.grid(row=2, column=1, padx=10, pady=(0, 20), sticky="ew")

        self.update_app_path_label()

        if tab_url is not None:
            self.entry_url: list[CTkEntry] = []
            self.label_url: list[CTkLabel] = []
            self.url_SV: list[StringVar] = []

            for i in range(len(tab_url)):
                self.url_SV.append(tk.StringVar(self, tab_url[i]))
                self.url_SV[i].trace("w", self.update_url_label)
                self.label_url.append(CTkLabel(self, text="Url", fg_color="transparent", text_color="#000"))
                self.entry_url.append(CTkEntry(self, text_color="#FFFFFF", textvariable=self.url_SV[i]))

                # self.entry_url[i].insert(0, tab_url[i])

                self.label_url[i].grid(row=2 * i + 3, column=0, padx=10, sticky="w")
                bottom_pading = 0
                if i == len(tab_url) - 1:  # If it's the last url we add a bottom padding
                    bottom_pading = 10
                self.entry_url[i].grid(row=2 * i + 4, column=0, padx=10, pady=(0, bottom_pading), sticky="ew")

                self.update_url_label(i)

            # TODO Add a button to add a new url

    def get_data(self) -> dict:
        """
        Get the data of the app
        :return: a dict with the path to the executable and the list of urls (if it's a browser)
        ex:
        {
            "path": "C:/Program Files/Google/Chrome/chrome.exe",
            "urls": ["https://www.google.com", "https://www.youtube.com"]
        }
        """
        data = {"path": self.app_path_SV.get()}
        if self.tab_url is not None:
            data["urls"] = [url.get() for url in self.entry_url]
        return data

    def open_explorer(self):
        """
        Open the explorer to choose a browser executable.
        If the user choose a file, the entry is updated with the path to the executable and we update the color
        """
        file_path = filedialog.askopenfilename(initialdir="/", title="Selectionner un executable",
                                               filetypes=(("executables", "*.exe"), ("all files", "*.*")))
        if file_path != "":
            self.app_path_SV.set(file_path)
        self.update_app_path_label()

    def __str__(self):
        if self.entry_path_app.get() == "":
            return "App (empty)"
        return "App " + get_application_name(self.entry_path_app.get())

    def update_app_path_label(self, *args):
        """
        Update the label and the entry color with the entry value
        """
        app_path = self.app_path_SV.get()
        self.label_path_app.configure(text=get_application_name(app_path))
        self.update_color(app_path)

    def update_url_label(self, *args):
        """
        Update the label and the entry color with the entry value
        """
        for i in range(len(self.entry_url)):
            url_path = self.url_SV[i].get()
            self.label_url[i].configure(text=get_site_name(url_path))

    def update_color(self, app_path):
        """
        Update the label and the entry color with the entry value.
        If the path doesn't exist, the color is red.
        :param app_path: the path to the executable
        """
        if not path.exists(app_path):
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
    """
    Show the template in a new window
    Each app is a frame with a label and an entry where the user can modify the path to the executable
    :param template_name: the name of the template to show
    """
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

        app[i].grid(row=i, column=0, padx=0, pady=10, sticky="new")

    window.mainloop()


def config_page():
    """
    Show the config page
    It's a ist of buttons, each button is a template and when clicked, it shows the template in a new window
    """
    window = CTk()
    window.configure(fg_color="#D9D9D9")
    window.title("QuikAccessHub - Configuration")
    window.title = TitleFrame(master=window, fg_color="#FFFFFF", title="Configuration")
    window.title.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

    window.geometry("400x300")
    window.resizable(False, True)

    window.grid_columnconfigure(0, weight=1)  # configure grid system
    window.grid_rowconfigure(2, weight=1)

    # Get the list of templates
    templates = get_template_list().keys()
    templates_button = []  # list of buttons for each template

    if len(templates) == 0:
        label = CTkLabel(window, text="Aucun template", font=CTkFont(family="Bahnschrift", size=20),
                         text_color="#353535", fg_color="#FFFFFF")
        label.grid(row=1, column=0, padx=20, pady=15)
    else:
        label = CTkLabel(window, text="Choisissez un template à configurer", corner_radius=7,
                         font=CTkFont(family="Bahnschrift", size=20), text_color="#353535", fg_color="#FFFFFF")
        label.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

    scroll = CTkScrollableFrame(master=window, fg_color="#FFFFFF")
    scroll.grid_columnconfigure(0, weight=1)
    scroll.grid(row=2, column=0, padx=20,pady=5, sticky="nsew")

    # Create a button for each template
    for template in templates:
        # To avoid the problem of the button always taking the last value of template,
        # we use a lambda function with a default argument
        templates_button.append(CTkButton(scroll, text=template,
                                          command=lambda template_used=template: show_template(template_used),
                                          font=CTkFont(family="Bahnschrift", size=15)))

    # Grid the buttons
    for i in range(len(templates_button)):
        templates_button[i].grid(row=i, column=0, padx=20, pady=10, sticky="nsew")

    window.mainloop()


def get_application_name(executable_path: str) -> str:
    """
    Get the name of the application from the executable path
    :param executable_path: the path to the executable (ex: C:/Program Files/Google/Chrome/chrome.exe)
    :return: the name of the application (ex: chrome)
    """
    app_name = os.path.splitext(os.path.basename(executable_path))[0]
    return app_name.capitalize()


def get_site_name(url: str) -> str:
    """
    Get the name of the site from the url.
    :param url: the url of the site (ex: https://www.google.com)
    :return: the name of the site (ex: google)
    """
    site_name = url.split("/")[2].split(".")[0]
    return site_name.capitalize()


def save_template(template_name: str, app: list[App | None], window: CTk):
    print("Saving template : " + template_name)
    new_template_data = [i.get_data() for i in app if i is not None]
    update_template(template_name, new_template_data)

    window.destroy()  # Close the window
