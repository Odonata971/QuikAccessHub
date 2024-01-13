import json


def get_template_list() -> dict:
    # Open and read the json file
    templates_file = "../json/templates.json"
    with open(templates_file, "r") as json_file:
        templates_list = json.load(json_file)
    return templates_list


def get_info_template(template_name: str) -> list[dict]:
    templates_list = get_template_list()
    return templates_list[template_name]


def update_template(template_name: str, new_template: list[dict]):
    templates_list = get_template_list()
    templates_list[template_name] = new_template
    with open("../json/templates.json", "w") as json_file:
        json.dump(templates_list, json_file, indent=4)
