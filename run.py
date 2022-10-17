from app import app
from cli_app import cliApp
import sys

isGUI = True

if len(sys.argv) > 1:
    isGUI = not sys.argv[1] in ['False', 'false', '0']

if isGUI:
    app = app.App()
else:
    app = cliApp.CliApp()

app.on_execute()
