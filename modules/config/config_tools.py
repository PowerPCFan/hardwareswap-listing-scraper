import importlib.util
import json
import os
from typing import List
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported
from dataclasses import dataclass

CONFIG_PY = "config.py"
CONFIG_JSON = "config.json"

def config_py_exists():
    return os.path.exists(CONFIG_PY)

def convert_py_to_json(config_py=CONFIG_PY, output_json=CONFIG_JSON):
    if config_py_exists():
        try:
            print(f"{YELLOW}Config.py file detected! This script now uses config.json. Attempting to migrate config.py -> config.json...{RESET}")
            
            # load config.py (chatgpt generated lol)
            spec = importlib.util.spec_from_file_location("config", config_py)
            if spec is None:
                raise ImportError(f"{RED}Error: Failed to load spec from {config_py}{RESET}")

            if spec.loader is None:
                raise ImportError(f"{RED}Error: Spec loader is None for {config_py}{RESET}")

            config = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config)

            # extract vars
            config_dict = {
                k: v for k, v in vars(config).items()
                if not k.startswith("__") and not callable(v)
            }

            # make config.json file
            with open(output_json, "w") as f:
                json.dump(config_dict, f, indent=4)
                
            # remove config.py file
            os.remove(CONFIG_PY)
            
            print(f"{GREEN}Successfully migrated config.py to config.json!{RESET}")
        except Exception as e:
            print(f"{RED}Error converting config.py to config.json: {e}{RESET}")

def ensure_all_values_are_present():
    default_config = {
        "reddit_id": "",
        "reddit_secret": "",
        "reddit_username": "",
        "mode": "firehose",
        "author_has": [
            "3060",
            "3060 Ti"
        ],
        "author_wants": [
            "PayPal"
        ],
        "openrouter_api_key": "",
        "author_has_llm_query": "",
        "author_wants_llm_query": "",
        "retrieve_older_posts": False,
        "tinyurl": False,
        "sl_expect_ovh": False,
        "sl_powerpcfan_xyz": False,
        "push_notifications": False,
        "topic_name": "",
        "sms": False,
        "gmail_address": "",
        "app_password": "",
        "sms_gateway": "",
        "phone_number": "",
        "webhook": False,
        "webhook_url": "",
        "webhook_ping": ""
    }
    
    deprecated_keys = [
        "firehose",
        "match",
        "match_llm"
    ]
        
    # load config.json
    with open(CONFIG_JSON, 'r') as f:
        config: dict = json.load(f)

    updated = False

    # add missing keys to config.json and set them to the default values
    for key, default_value in default_config.items():
        if key not in config:
            print(f"{RED}Key '{key}' was not found in your config.json file. Adding...{RESET}")
            config[key] = default_value
            updated = True
    
    # remove keys that were once used but are no longer needed
    for key in deprecated_keys:
        if key in config:
            print(f"{YELLOW}Deprecated key '{key}' was found in your config.json file. Removing...{RESET}")
            config.pop(key, None)
            updated = True

    if updated:
        with open(CONFIG_JSON, 'w') as f:
            json.dump(config, f, indent=4)

@dataclass
class Config:
    # type stuff
    reddit_id: str
    reddit_secret: str
    reddit_username: str

    mode: str

    author_has: List[str]
    author_wants: List[str]
    
    openrouter_api_key: str
    author_has_llm_query: str
    author_wants_llm_query: str

    retrieve_older_posts: bool
    
    tinyurl: bool
    sl_expect_ovh: bool
    sl_powerpcfan_xyz: bool
    
    push_notifications: bool
    topic_name: str

    sms: bool
    gmail_address: str
    app_password: str
    sms_gateway: str
    phone_number: str
    
    webhook: bool
    webhook_url: str
    webhook_ping: str

    # function to load the vars from config.json
    @staticmethod
    # def load(json_path=CONFIG_JSON) -> "Config":
    def load(json_path="config.json") -> "Config":
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"{RED}Error: {json_path} not found.{RESET}")
        with open(json_path) as f:
            data = json.load(f)
        return Config(**data)
