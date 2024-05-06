import subprocess
from template_service import get_template_list

templates_list = ""


def launch_applications(template_name: str):
    """
    Launch the applications of the template used
    :param template_name: the name template used
    """
    global templates_list

    # Reload the templates list every time this function is called
    templates_list = get_template_list()

    # Loop through the json file
    template_data = templates_list[template_name]

    for app in template_data:

        # if the app is a browser, open the urls in tabs
        # a browser is a special case because it has a list of urls
        if "urls" in app:
            browser_path = app["path"]
            urls_to_open = app["urls"]
            command = [browser_path] + [" --new-tab " + url for url in urls_to_open]

            try:
                subprocess.Popen(command)
            except FileNotFoundError:
                print(browser_path + " not found")

        # else, it's a normal app
        else:
            try:
                subprocess.Popen(app["path"])
            except FileNotFoundError:
                print(app["path"] + " not found")