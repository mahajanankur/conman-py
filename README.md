# Pyconman
[![PyPI](https://img.shields.io/pypi/v/pyconman?logo=PyPI)](https://badge.fury.io/py/pyconman)
![PyPI - Status](https://img.shields.io/pypi/status/pyconman?logo=PyPI)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyconman?logo=PyPI)
[![License](https://img.shields.io/badge/code%20license-Apache%20License%2C%202.0-lightgrey?logo=GitHub)](https://github.com/mahajanankur/pyconman-py/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/pyconman)](https://pepy.tech/project/pyconman)

Pyconman is a useful package for managing JSON configurations in Python-based applications. The package provides a system for managing different configurations for different environments, making it easier to handle secure and critical configurations.

- **Environment-specific configurations:** Pyconman allows you to manage different configurations for different environments (e.g., development, staging, production), making it easier to handle environment-specific configurations.

- **Simpler configuration management:** Pyconman provides a simple and convenient way to manage and access configurations in your Python code, without having to write custom code for handling different configurations.

- **Security:** Pyconman helps you manage secure and critical configurations by allowing you to store sensitive information (e.g., API keys, passwords) in a separate configuration file that is not checked into source control.

- **Easy to use:** Pyconman is easy to use and requires minimal setup, making it a great choice for developers who want a simple and reliable way to manage configurations in their Python applications.

### Installation

Pyconman requires [Python](https://www.python.org/) to run.

To use pyconman, you can install it using pip by running the command.
```sh
$ pip install pyconman
```
Once installed, you can create a Python virtual environment by running the command in your project directory. This will create a virtual environment and activate it.
```sh
python3 -m venv .venv && source .venv/bin/activate 
```
## Usage
Next, create a folder called `configs` in your `project root directory`, and create a file called `default.json` in it. This file will contain the default configuration properties for your application. If you want to use a different environment, you can pass that environment's name in the `ENV` variable to override the specific properties for that environment. Please look in the example folder for further information.

Here are two sample JSON configurations that you can use with the Pyconman package:

**default.json:**
```json
{
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "dbuser",
        "password": "dbpassword",
        "database_name": "mydb"
    },
    "api_key": "1234567890",
    "log_level": "debug"
}
```
**production.json:**

```json
{
    "database": {
        "host": "prod-db-host",
        "username": "prod-db-user",
        "password": "prod-db-password",
        "props": {
            "timeout": 10000,
            "trans": 100
        }
    }
}
```

To load the configuration in your application, you can use the `ConfigLoader` class provided by pyconman. Here's an example of how you can use it `test.py`:
```python
from pyconman import ConfigLoader

# Load the configuration in the application scope.
config = ConfigLoader.get_config()
prop_1 = config.get("prop_1")

# Access nested JSON properties
prop_n = config["prop_1"]["prop_2"]["prop_n"]
```

---
License
----
**Apache 2.0**