import os
import sys

# globals.py
# Check if we're running as a script or a frozen exe
application_path = ""
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

json_path = os.path.join(application_path, 'json/templates.json')

logo_path = os.path.join(application_path, 'icons', 'QuikAccessHub_logo.ico')
