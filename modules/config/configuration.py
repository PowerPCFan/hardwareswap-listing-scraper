import modules.config.config_tools as conftools
import modules.versioning_tools as versioning_tools

config = conftools.Config.load()

remote_version = versioning_tools.get_remote_version()
local_version = versioning_tools.get_local_version()
