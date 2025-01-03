import os
username=os.environ.get("MONGO_USERNAME")
password=os.environ.get("MONGO_PASSWORD")
cluster_name=os.environ.get("MONGO_CLUSTER_NAME")

mongo_conn_string = f"mongodb+srv://{username}:{password}@chandra-dev.pcpogvu.mongodb.net/{cluster_name}?retryWrites=true&w=majority"