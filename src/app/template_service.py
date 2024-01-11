import json


def get_template_list() -> dict:
    # Open and read the json file
    templates_file = "../json/templates.json"
    with open(templates_file, "r") as json_file:
        templates_list = json.load(json_file)
    return templates_list
