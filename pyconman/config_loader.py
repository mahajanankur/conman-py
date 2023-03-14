import os, json
from dotenv import load_dotenv

dir_path = os.path.join(os.getcwd(), "configs")

# from utils.json_util import JsonUtils

load_dotenv()  # load environment variables from .env file

class ConfigLoader:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._config = cls.load_config()
        return cls._instance

    @staticmethod
    def load_config(env = "local"):
        print(f"directory path in load_config = {dir_path}")
        try:
            # Determine the environment
            environment = os.environ.get('ENV', env)
            # Load the default configuration file
            with open(f'{dir_path}/default.json', 'r') as f:
                default_configs = json.load(f)
            
            if environment != "local":
                # Load the environment-specific configuration file
                with open(f'{dir_path}/{environment}.json', 'r') as f:
                    env_config = json.load(f)
                # Merge the default and dynamic properties.
                merged_configs = ConfigLoader.__merge_json(default_configs, env_config)
            else:
                merged_configs = default_configs
            
            return merged_configs

        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading configurations: {str(e)}")

    @staticmethod
    def get_config(env = "local"):
        if ConfigLoader._config is None:
            ConfigLoader._config = ConfigLoader.load_config(env=env)
        return ConfigLoader._config
    
    @staticmethod
    def __merge_json(json1, json2):
        # Recursively merges two JSON objects
        if isinstance(json1, dict) and isinstance(json2, dict):
            merged = json1.copy()
            for key, value in json2.items():
                if key in merged:
                    merged[key] = ConfigLoader.__merge_json(merged[key], value)
                else:
                    merged[key] = value
            return merged
        else:
            return json2