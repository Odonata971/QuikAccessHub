from os.path import basename

from customtkinter import *
from template_service import *
from os import path


def show_template(template_to_config: str):
    print("Configuring template : " + template_to_config)
    # Get the template data
    template_data = get_info_template(template_to_config)
    window = CTk()
    window.configure(fg_color="#D9D9D9")
    window.title("QuikAccessHub - " + template_to_config)
    title = TitleFrame(master=window, fg_color="#FFFFFF", title="Config of " + template_to_config)
    title.grid(row=0, column=0, padx=20, pady=10, sticky="new")

    window.geometry("600x500")
    window.resizable(False, False)

    window.grid_columnconfigure(0, weight=1)  # configure grid system
    window.grid_rowconfigure(1, weight=1)

    scroll = CTkScrollableFrame(master=window, fg_color="transparent")
    scroll.grid(row=1, column=0, padx=20, sticky="snew")
    scroll.grid_columnconfigure(0, weight=1)

    try:
        browser_frame = Browser(master=scroll, browser_info=template_data["browser"], fg_color="#FFFFFF")
        browser_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
    except KeyError:
        pass

    try:
        for i in range(len(template_data["others"])):
            app = App(master=scroll, app_path=template_data["others"][i], fg_color="#FFFFFF")
            app.grid(row=i + 2, column=0, padx=20, pady=10, sticky="ew")
    except KeyError:
        pass

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


def get_application_name(executable_path: str)->str:
    return os.path.splitext(os.path.basename(executable_path))[0]


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


class Browser(CTkFrame):
    def __init__(self, master, browser_info: dict, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)  # configure grid system

        self.path_to_browser = StringVar()
        self.label_path_browser = CTkLabel(self, text="Navigateur", fg_color="transparent", text_color="#000")
        self.entry_path_browser = CTkEntry(self, placeholder_text="Chemin vers l'executable du navigateur",
                                           textvariable=self.path_to_browser, text_color="#FFFFFF")
        self.entry_path_browser.insert(0, browser_info["path"])

        self.label_path_browser.grid(row=1, column=0, padx=(10, 2), sticky="w")
        self.entry_path_browser.grid(row=2, column=0, padx=10, pady=(0, 20), sticky="ew")

        self.url: list[StringVar] = []
        self.entry_url: list[CTkEntry] = []
        self.label_url: list[CTkLabel] = []

        for i in range(len(browser_info["urls"])):
            self.url.append(StringVar())
            self.label_url.append(CTkLabel(self, text="Url", fg_color="transparent", text_color="#000"))
            self.entry_url.append(CTkEntry(self, textvariable=self.url[i], text_color="#FFFFFF"))
            self.entry_url[i].insert(0, browser_info["urls"][i])

            self.label_url[i].grid(row=2 * i + 3, column=0, padx=10, sticky="w")
            bottom_pading = 0
            if i == len(browser_info["urls"]) - 1:  # If it's the last url we add a bottom padding
                bottom_pading = 10
            self.entry_url[i].grid(row=2 * i + 4, column=0, padx=10, pady=(0, bottom_pading), sticky="ew")

        # TODO Add a button to add a new url


class App(CTkFrame):
    def __init__(self, master, app_path: str, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)  # configure grid system

        self.path_to_app = StringVar()
        self.label_path_app = (CTkLabel(self, text=get_application_name(app_path), fg_color="transparent", text_color="#000"))
        self.entry_path_app = (CTkEntry(self, placeholder_text="Chemin vers l'executable du navigateur",
                                        textvariable=self.path_to_app, text_color="#FFFFFF"))
        (self.entry_path_app.insert(0, app_path))

        self.label_path_app.grid(row=1, column=0, padx=(10, 2), sticky="w")
        self.entry_path_app.grid(row=2, column=0, padx=10, pady=(0, 20), sticky="ew")

        # TODO Add a button to add an app
