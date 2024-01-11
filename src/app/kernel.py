import subprocess
from template_service import get_template_list

templates_list = get_template_list()


def launch_applications(template_used: str):
    """
    Launch the applications of the template used
    :param template_used: the name template used
    """

    # Loop through the json file
    template_data = templates_list[template_used]

    for category in template_data:

        # open all the urls in the browser in tabs
        if category == "browser":
            browser_path = template_data[category]["path"]
            urls_to_open = template_data[category]["urls"]
            command = [browser_path] + [" --new-tab " + url for url in urls_to_open]

            try:
                subprocess.Popen(command)
            except FileNotFoundError:
                print(browser_path + " not found")

        else:
            # open all the remaining applications
            for j in range(len(template_data[category])):
                try:
                    subprocess.Popen(template_data[category][j])
                except FileNotFoundError:
                    print(template_data[category][j] + " not found")
