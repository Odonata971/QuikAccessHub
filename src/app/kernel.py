import subprocess
import json

# Open and read the json file
templates_file = "../json/templates.json"
with open(templates_file, "r") as json_file:
    templates_list = json.load(json_file)["templates"]


# Create a function to launch the selected applications
def launch_applications(template_used: str):
    for i in range(len(templates_list[template_used]["paths"])):
        try:
            # Launch each application in the list
            subprocess.Popen([templates_list[template_used]["paths"][i]])
        except Exception as e:
            print("non")
