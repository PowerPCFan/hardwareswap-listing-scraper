# this is called configuration.py not config.py because the file that contains secrets used to be called config.py
# it doesnt exist anymore but i dont want to remove from gitignore to be safe

import modules.config.config_tools as conftools
import modules.versioning_tools as versioning_tools

config = conftools.Config.load()

remote_version = versioning_tools.get_remote_version()
local_version = versioning_tools.get_local_version()