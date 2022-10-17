import sys

isGUI = True
if len(sys.argv) > 1:
    isGUI = not sys.argv[1] in ['False', 'false', '0']

if isGUI:
    from app import app
    app = app.App()
else:
    from cli_interface import cliInterface
    app = cliInterface.CliInterface()

app.on_execute()
