import os

def is_browser(application_path):
    known_browsers = ['chrome', 'firefox', 'safari', 'edge', 'opera', 'brave']
    application_name = os.path.splitext(os.path.basename(application_path))[0]
    return application_name.lower() in known_browsers

# Test the function
application_path = "BraveSoftware/Brave-Browser/Application/brave.exe"
print(is_browser(application_path))