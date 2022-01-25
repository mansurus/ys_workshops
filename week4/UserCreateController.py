import User
import JsonLoadController
import re
from similarityHelper import shared_chars
class UserCreate:
    def __init__(self,jsonFile):
        self.jsonFile = jsonFile
        self.jsonResult = self.jsonGetter()

    def jsonGetter(self):        
        jsonUser = JsonLoadController.JsonReader(self.jsonFile)
        jsonUsers = jsonUser.getData        
        allUsers = []
        for user in jsonUsers:            
            email = user["email"]
            username = user["username"]
            fullName = user["profile"]["name"]
            emailuserlk = 1 if shared_chars(re.search(r'([^@]+)', user["email"])[0],user["username"])>2 else 0
            usernamelk = 1 if shared_chars(user["username"],user["profile"]["name"])>2 else 0
            bYear = re.findall(r'^[0-9]{3}[a-zA-Z0-9]',user["profile"]["dob"])[0]
            bMonth = re.findall(r'^[^-]*-([^-]*).*', user["profile"]["dob"])[0]
            bDay = re.findall(r'..$', user["profile"]["dob"])[0]
            country = re.findall(r'(?<=,.)[^,]*$', user["profile"]["address"])[0]
            isActive = 1
            userToAdd = User.User(email, username, fullName, emailuserlk, usernamelk, bYear, bMonth, bDay, country, isActive)
            allUsers.append(userToAdd)
        return allUsers