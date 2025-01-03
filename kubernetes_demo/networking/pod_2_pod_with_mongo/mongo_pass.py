import os
mongo_user=os.environ.get("MONGO_USERNAME", "adminuser")
mongo_password=os.environ.get("MONGO_PASSWORD", "chandra")
mongo_address=os.environ.get("MONGO_ADDRESS")

mongo_connection_string = f"mongodb://{mongo_user}:{mongo_password}@{mongo_address}:27017/fruits_db?authSource=admin"