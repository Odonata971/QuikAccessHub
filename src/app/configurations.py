import json

# Open and read the json file
templates_file = "../json/templates.json"
with open(templates_file, "r") as json_file:
    templates_list = json.load(json_file)

# configure / change the templates
