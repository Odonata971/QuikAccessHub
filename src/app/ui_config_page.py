from customtkinter import *
from template_service import *


def show_template(template_to_config: str):
    print("Configuring template : " + template_to_config)
    # Get the template data
    template_data = get_info_template(template_to_config)


def config_page():
    # Display an error message
    window = CTk()
    window.configure(fg_color="#D9D9D9")
    window.title("QuikAccessHub - Config Page")
    window.title = TitleFrame(master=window, fg_color="#FFFFFF")
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
