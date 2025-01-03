import os
mongo_user=os.environ.get("MONGO_USERNAME", "chandra")
mongo_password=os.environ.get("MONGO_PASSWORD", "chandra")

mongo_connection_string = f"mongodb://{mongo_user}:{mongo_password}@mongodb:27017/fruits_db?authSource=admin"