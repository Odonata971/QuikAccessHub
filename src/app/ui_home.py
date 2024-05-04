from kernel import launch_applications
from component import TitleFrame
from template_service import get_template_list
from customtkinter import *
import ui_config_page as config
import ui_help as help
import globals


class App(CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(globals.logo_path)
        self.geometry("600x450")
        self.title("QuikAccessHub")

        self.grid_rowconfigure(3, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.title = TitleFrame(master=self,title="QuikAccessHub", fg_color="#FFFFFF")
        self.title.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        self.templates = TemplatesFrame(master=self, fg_color="#FFFFFF")
        self.templates.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

        self.configure_templates = ConfigureTemplates(master=self, fg_color="#FFFFFF")
        self.configure_templates.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")


class TemplatesFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.templates = []  # list of buttons for each template
        self.grid_rowconfigure(6, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        # Get the list of templates
        templates = get_template_list().keys()

        # add widgets onto the frame, for example:
        self.label = CTkLabel(self, text="Choose a template", font=CTkFont(family="Bahnschrift", size=20),
                              text_color="#353535")
        if len(templates) == 0:
            self.label = CTkLabel(self, text="No template found", font=CTkFont(family="Bahnschrift", size=20),
                                  text_color="#353535")
        # Create a button for each template
        for template in templates:
            # To avoid the problem of the button always taking the last value of template,
            # we use a lambda function with a default argument
            self.templates.append(CTkButton(self, text=template,
                                            command=lambda template_used=template: launch_applications(template_used),
                                            font=CTkFont(family="Bahnschrift", size=15)))

        self.label.grid(row=0, column=0, padx=20, pady=15)
        # Grid the buttons
        for i in range(len(self.templates)):
            self.templates[i].grid(row=i + 1, column=0, padx=20, pady=5)


class ConfigureTemplates(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(2, weight=1)
        self.configure_templates = CTkButton(self, text="Configure Templates", command=config.config_page,
                                             font=CTkFont(family="Bahnschrift", size=15))
        self.help = CTkButton(self, text="Help", command=help.ui_page,
                              font=CTkFont(family="Bahnschrift", size=15))
        self.configure_templates.grid(row=0, column=0, padx=70, pady=10)
        self.help.grid(row=0, column=1, padx=45, pady=10)


if __name__ == "__main__":

    # We check if the json file is present. If not, we create it blank
    if not os.path.isfile(globals.json_path):
        print("The json file is not present")
        with open(globals.json_path, "w") as json_file:
            json_file.write("{}")

    # Create the app
    app = App()
    app.configure(fg_color="#D9D9D9")
    app.mainloop()
