import json

class JsonReader:
    def __init__(self,jsonFile):
        self.jsonFile = jsonFile
        self.getData = self.getUsers()

    def getUsers(self):
        with open(self.jsonFile) as userDataFromJson:
            userData = json.load(userDataFromJson)
            return userData
    