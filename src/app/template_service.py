import json


def get_template_list() -> dict:
    """
        Get the list of templates in the json file
    """
    # Open and read the json file
    templates_file = "../json/templates.json"
    with open(templates_file, "r") as json_file:
        templates_list = json.load(json_file)
    return templates_list


def get_info_template(template_name: str) -> list[dict]:
    """
        Get the info of a template in the templates_list
        :param template_name: the template's name to use
    """
    templates_list = get_template_list()
    return templates_list[template_name]


def update_template(template_name: str, new_template: list[dict]):
    """
        Update the template's info in the json file
        :param template_name: the template's name to use
        :param new_template: the new template's info
    """
    templates_list = get_template_list()
    templates_list[template_name] = new_template
    with open("../json/templates.json", "w") as json_file:
        json.dump(templates_list, json_file, indent=4)
