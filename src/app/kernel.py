import subprocess
import json

# Open and read the json file
templates_file = "../json/templates.json"
with open(templates_file, "r") as json_file:
    templates_list = json.load(json_file)


# Launch the applications
def launch_applications(template_used: str):
    print(templates_list)
    # Loop through the json file
    template_data = templates_list[template_used]
    print(template_data)
    for category in template_data:
        print(category)
        try:
            # open all the urls in the browser in tabs
            if category == "browser":
                browser_path = template_data[category]["path"]
                print(browser_path)
                urls_to_open = template_data[category]["urls"]
                command = [browser_path] + [" --new-tab " + url for url in urls_to_open]
                subprocess.Popen(command)
                pass

            # open all the remaining applications
            for j in range(len(template_data[category])):
                subprocess.Popen(template_data[category][j])

        except Exception as e:
            print("non")
