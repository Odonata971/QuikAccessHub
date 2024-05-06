from customtkinter import CTk, CTkScrollableFrame, CTkButton

from component import *
from component import TitleFrame
from template_service import *
from ui_config_template import ConfigurationWindow


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

    window.geometry("600x450")
    window.resizable(False, True)

    window.grid_columnconfigure(0, weight=1)  # configure grid system
    window.grid_rowconfigure(2, weight=1)

    # Get the list of templates
    templates = get_template_list().keys()
    templates_button = []  # list of buttons for each template

    if len(templates) == 0:
        label = CTkLabel(window, text="None templates found", font=CTkFont(family="Bahnschrift", size=20),
                         text_color="#353535", fg_color="#FFFFFF")
        label.grid(row=1, column=0, padx=20, pady=15)
    else:
        label = CTkLabel(window, text="Choose your template to configure", corner_radius=7,
                         font=CTkFont(family="Bahnschrift", size=20), text_color="#353535", fg_color="#FFFFFF")
        label.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

    scroll = CTkScrollableFrame(master=window, fg_color="#FFFFFF")
    scroll.grid_columnconfigure(0, weight=1)
    scroll.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")

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


def show_template(template_name: str):
    """
    Show the template in a new window
    Each app is a frame with a label and an entry where the user can modify the path to the executable
    :param template_name: the name of the template to show
    """
    window = ConfigurationWindow(template_name)
    window.mainloop()
