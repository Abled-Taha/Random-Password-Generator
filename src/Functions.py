import os
import json
import Encryptor
import RandomPasswordGenerator as RPG
import pymongo

url = "localhost"
port = 27017
client = pymongo.MongoClient(url, port)
db = client.RandomPasswordGenerator
users = db.users
credentials = db.credentials

def validateSignIn(email, password):
    try:
        user = users.find_one({"email":email})
        dbpassword = user["password"]
    except:
        return False
    if password == dbpassword:
        return True
    else:
        return False

def validateSignUp(email, password, confirmPassword):
    if password == confirmPassword:
        pass
    if email != "":
        pass
    if email.__contains__('@'):
        pass
    else:
        return False
    allDone = createAccount(email, password)

    return allDone

def createAccount(email, password):
    user = users.find_one({"email":email})
    if user == None:
        db.users.insert_one({"email":email, "password":password})
        return True
    else:
        return False

def Details(email):
    # Returning Key Count
    usercredentials = credentials.find_one({"email":email})
    passwords = usercredentials["passwords"]
    keyCount = len(passwords.keys())

    # Returning Password Name
    keyList = []
    for key, value in passwords.items():
        keyList.append(key)

    return keyCount, keyList

def getPass(objectName, email):
    usercredentials = credentials.find_one({"email":email})
    passwords = usercredentials["passwords"]
    password = passwords[f"{objectName}"]

    return password

def createPassword(Name, Characters, Capital, Small, Numbers, Symbols, email):
    usercredentials = credentials.find_one({"email":email})
    passwords = usercredentials["passwords"]
    password = RPG.generateNewPassword(Characters, Capital, Small, Numbers, Symbols)
    os.chdir("Files/Accounts")

    passwords[f"{Name}"] = password
    db.credentials.update_one({"_id":usercredentials["_id"]}, {"$set":{"passwords":passwords}})

def deletePassword(Name, email):
    usercredentials = credentials.find_one({"email":email})
    passwords = usercredentials["passwords"]
    try:
        del passwords[f"{Name}"]
        db.credentials.update_one({"_id":usercredentials["_id"]}, {"$set":{"passwords":passwords}})
    except:
        return False
    return True

def deleteUser(email, password):
    try:
        user = users.find_one({"email":email})
        dbpassword = user["password"]
    except:
        return False
    if password == dbpassword:
        db.users.delete_one({"_id":user["_id"]})
        return True
    else:
        return False