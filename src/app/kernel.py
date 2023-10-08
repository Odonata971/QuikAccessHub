import subprocess
import json

# Open and read the json file
templates_file = "../json/templates.json"
with open(templates_file, "r") as json_file:
    templates_list = json.load(json_file)["templates"]


res_wanted = str(int(input("Quel est votre choix ? (1 ou 2) : ")))
# Create a function to launch the selected applications
def launch_applications():
    for i in range(len(templates_list[res_wanted]["paths"])):
        try:
            # Launch each application in the list
            subprocess.Popen([templates_list[res_wanted]["paths"][i]])
        except Exception as e:
            print("non")
