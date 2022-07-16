import json
import os

class profile:
    def __init__(self, profile_id:str):
        self.id = profile_id
    
    def create(self):
        root_directory = os.getcwd()
        os.chdir("profiles")
        file_name = f"{self.id}.json"
        with open(file_name, 'w') as f:
            file_content = {"id": self.id, "money": 0}
            file_content_json = json.dumps(file_content)
            f.write(file_content_json)
        os.chdir(root_directory)

    def get(self):
        root_directory = os.getcwd()
        os.chdir("profiles")
        file_name = f"{self.id}.json"
        with open(file_name, "r") as f:
            file_content = f.read()
            file_content_json = json.loads(file_content)
        os.chdir(root_directory)
        return file_content_json

    def change(self, new_profile:dict):
        root_directory = os.getcwd()
        os.chdir("profiles")
        file_name = f"{self.id}.json"
        with open(file_name, 'w') as f:
            file_content_json = json.dumps(new_profile)
            f.write(file_content_json)
        os.chdir(root_directory)
