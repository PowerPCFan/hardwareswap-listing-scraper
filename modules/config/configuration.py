# this is called configuration.py not config.py because the file that contains secrets used to be called config.py
# it doesnt exist anymore but i dont want to remove from gitignore to be safe

import modules.config.config_tools as conftools

config = conftools.Config.load()