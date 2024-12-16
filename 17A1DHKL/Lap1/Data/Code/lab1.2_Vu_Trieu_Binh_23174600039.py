import json
class JSONReader:
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = None
    def read_json(self):
        with open(self.file_path, 'r',encoding = "UTF-8") as file:
            self.data = json.load(file)

    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name :{user['name']}, age: {user['age']}, \
                Address : {user['addres']}")
path = r"Lap1/Data/Data1/users.json"
reader = JSONReader(path)
reader.read_json()
reader.display_data()