from pyconman import ConfigLoader

# Load the configuration in the application scope.
config = ConfigLoader.get_config()

database = config.get("database")

# Access nested JSON properties
db_user = database["username"]

print(f"database = {database} | db_user = {db_user}")