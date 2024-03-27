import time
import tkinter as tk
from customtkinter import *

from src.app.component import *
from template_service import *
from os import path
from tkinter.messagebox import askyesno

CHANGE_MADE: bool = False


class ConfigurationWindow(CTk):
    """
    The window to configure a template
    """

    def __init__(self, template_name, **kwargs):
        super().__init__(**kwargs)
        self.no_app = None
        self.template_name = template_name
        self.add_app_button = None
        self.save_button = None
        self.scroll = None
        # Get the template data
        self.template_data: list[dict] = get_info_template(self.template_name)
        self.app: list[ApplicationFrame] = []
        self.btn_delete: list[CTkButton] = []

        self.configure(fg_color="#D9D9D9")
        self.title("QuikAccessHub - " + self.template_name)
        self.geometry("700x500")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)  # configure grid system
        self.grid_rowconfigure(3, weight=1)

        self.build_widget()

        self.mainloop()

    def build_widget(self):
        global CHANGE_MADE
        title = TitleFrame(master=self, fg_color="#FFFFFF", title="Config of " + self.template_name)
        self.scroll = CTkScrollableFrame(master=self, fg_color="transparent")
        self.save_button = CTkButton(master=self, text="Save", command=lambda: self.save_template())
        self.add_app_button = CTkButton(master=self, text="Add an app", command=lambda: self.add_app(),
                                        fg_color="#009400", hover_color="#007B00")
        self.no_app = CTkLabel(self.scroll, text="Aucun template", font=CTkFont(family="Bahnschrift", size=20),
                               text_color="#353535", fg_color="#FFFFFF")

        self.scroll.grid_columnconfigure(1, weight=1)

        title.grid(row=0, column=0, padx=20, pady=10, sticky="new")
        self.save_button.grid(row=1, column=0, padx=20, pady=10, sticky="new")
        self.add_app_button.grid(row=2, column=0, padx=20, pady=10, sticky="new")
        self.scroll.grid(row=3, column=0, padx=20, sticky="snew")

        CHANGE_MADE = False
        self.create_app_widget()

    def create_app_widget(self):
        for i in range(len(self.template_data)):
            if "urls" in self.template_data[i]:
                self.app.append(ApplicationFrame(master=self.scroll, app_path=self.template_data[i]["path"],
                                                 tab_url=self.template_data[i]["urls"], fg_color="#FFFFFF"))
            else:
                self.app.append(ApplicationFrame(master=self.scroll, app_path=self.template_data[i]["path"],
                                                 fg_color="#FFFFFF"))
        self.show_app()

    def add_app(self):
        self.app.insert(0, ApplicationFrame(master=self.scroll, app_path="", fg_color="#FFFFFF"))
        self.show_app()

    def show_app(self):

        if len(self.app) == 0:
            self.no_app.grid(row=0, column=0, padx=20, pady=10, sticky="new")
        else:
            self.no_app.grid_remove()

        for btn in self.btn_delete:
            btn.grid_remove()
        self.btn_delete = []

        for i in range(len(self.app)):
            self.app[i].grid_remove()
            if self.app[i] is None:
                continue
            self.btn_delete.append(CTkButton(self.scroll, text="X", fg_color="#F00", width=1, hover_color="#C00",
                                             command=lambda index=i: self.delete_app(index)))
            self.btn_delete[i].grid(row=i + 1, column=0, pady=20, sticky="new")
            self.app[i].grid(row=i + 1, column=1, padx=20, pady=10, sticky="new")

    def save_template(self):
        new_template_data = [i.get_data() for i in self.app if i is not None]
        update_template(self.template_name, new_template_data)
        time.sleep(0.5)
        self.destroy()  # Close the window

    def delete_app(self, index: int):
        answer: bool = askyesno(title="Confirmation", message="Delete this app ?\n" + self.app[index].app_path_SV.get())
        if answer:
            self.app[index].destroy()
            self.app.pop(index)
            self.show_app()

class ApplicationFrame(CTkFrame):
    """
    A frame to configure an application
    """

    def __init__(self, master, app_path: str, tab_url=[], **kwargs):
        super().__init__(master, **kwargs)

        self.app_path_SV: StringVar = tk.StringVar(self, app_path)
        self.app_path_SV.trace("w", self.update_app_path_label)

        self.grid_columnconfigure(1, weight=3)  # configure grid system

        self.label_path_app = CTkLabel(self, fg_color="transparent", text_color="#000")
        self.entry_path_app = CTkEntry(self, text_color="#FFF", textvariable=self.app_path_SV)
        self.explorer_button = CTkButton(self, text="Browse", command=self.open_explorer)

        self.label_path_app.grid(row=1, column=1, padx=(10, 2), sticky="w")
        self.entry_path_app.grid(row=2, column=1, padx=10, pady=(0, 20), sticky="ew")
        self.explorer_button.grid(row=2, column=2, padx=10, pady=(0, 20), sticky="ew")

        self.update_app_path_label()

        self.entry_url = None
        self.url_internet: list[str] = tab_url

        if len(self.url_internet) != 0:
            self.add_url()
        else:
            self.add_entry_url = CTkButton(self, text="Add an url", command=lambda: self.add_url(from_user=True))
            self.add_entry_url.grid(row=3, column=1, padx=10, pady=(0, 20), sticky="ew")

    def get_data(self) -> dict:
        """
        Get the data of the app
        :return: a dict with the path to the executable and the list of urls (if it's a browser)
        ex:
        {
            "path": "C:/Program Files/Google/Chrome/chrome.exe",
            "urls": ["https://www.python.org/", "https://customtkinter.tomschimansky.com/"]
        }
        """
        if self.app_path_SV is not None:
            data = {"path": self.app_path_SV.get()}
            if self.entry_url is not None:
                data["urls"] = self.entry_url.get("0.0", "end").split("\n")
                for url in data["urls"]:
                    if url == "":
                        data["urls"].remove(url)
            return data

    def open_explorer(self):
        """
        Open the explorer to choose a browser executable.
        If the user choose a file, the entry is updated with the path to the executable and we update the color
        """
        file_path = filedialog.askopenfilename(initialdir="/", title="Select an executable",
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
        global CHANGE_MADE
        app_path = self.app_path_SV.get()
        self.label_path_app.configure(text=get_application_name(app_path))
        self.update_color(app_path)
        CHANGE_MADE = True

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

    def add_url(self, from_user=False):
        """
        Add the text area to enter an url
        :param from_user: if the user add an url or if it's from the template
        :return:
        """
        if from_user:
            self.add_entry_url.grid_remove()

        self.entry_url = CTkTextbox(self, text_color="#FFF")
        self.entry_url.insert("0.0", "\n".join(self.url_internet))
        self.entry_url.grid(row=3, column=1, padx=10, pady=(0, 20), sticky="ew")


def get_application_name(executable_path: str) -> str:
    """
    Get the name of the application from the executable path
    :param executable_path: the path to the executable (ex: C:/Program Files/Google/Chrome/chrome.exe)
    :return: the name of the application (ex: Chrome)
    """
    return os.path.splitext(os.path.basename(executable_path))[0].capitalize()


def get_site_name(url: str) -> str:
    """
    Get the name of the site from the url.
    :param url: the url of the site (ex: https://www.google.com)
    :return: the name of the site (ex: Google)
    """
    if url == "":
        return "-"
    return url.split("/")[2].split(".")[0].capitalize()
