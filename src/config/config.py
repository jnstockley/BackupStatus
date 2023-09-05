import os
import tomllib

PROFILES = ['dev', 'beta', 'test', 'prod']
PROFILE = 'dev'
CONFIG: dict = {}


def set_profile():
    profile = os.environ['BACKUP_SERVER']
    if profile in PROFILES:
        global PROFILE
        PROFILE = profile


def load_config():
    with open('conf/config.toml', 'rb') as f:
        global CONFIG
        CONFIG = tomllib.load(f)


def get_value(key: str):
    if CONFIG != {}:
        params = key.split(".")
        if len(params) > 2:
            raise ConfigException(f"{key} is not a valid key")
        try:
            return CONFIG[params[0]][PROFILE][params[1]]
        except KeyError:
            raise ConfigException(f"Key {key} is not a present in the loaded config file")
    else:
        raise ConfigException("Config Not loaded, run `load_config`")


class ConfigException(Exception):
    def __init__(self, message):
        super().__init__(message)
