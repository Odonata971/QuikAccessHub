from customtkinter import CTk, CTkFont, CTkButton

from component import *
from component import TitleFrame

def ui_page():
    """
    Show the ui page
    It's just a help to inform the user how to use the app properly
    """
    window = CTk()
    window.configure(fg_color="#D9D9D9")
    window.title("QuikAccessHub - Help")
    window.title = TitleFrame(master=window, fg_color="#FFFFFF", title="Help")
    window.title.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

    window.geometry("600x300")
    window.resizable(False, False)

    window.grid_columnconfigure(0, weight=1)  # configure grid system
    window.grid_rowconfigure(2, weight=1)

    text  = """
            This app is there to help you to launch your applications faster.
            In order to get started, you need to configure a template.
            A template is a group of applications that you want to launch together.
            To configure a template, click on the "Configuration" button.
            You can then add applications to the template. 
            Browser can be added also with whatever website's urls you want
            Once you have configured a template, you can launch it by clicking on the "Launch" button.
            You can have a grand total of 5 templates.
            Enjoy!
            """

    # Create a help text to explain how to use the app
    help_text = CTkLabel(window, text=text, corner_radius=7, justify="left",
                        font=CTkFont(family="Bahnschrift", size=15), text_color="#353535", fg_color="#FFFFFF")
    help_text.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

    window.mainloop()


