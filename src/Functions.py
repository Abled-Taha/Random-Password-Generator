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
    if password == (Encryptor.Decrypt(dbpassword)):
        return True
    else:
        return False

def validateSignUp(email, password, confirmPassword):
    temp = 0
    if password == confirmPassword:
        temp += 1
    if email != "":
        temp += 1
    if email.__contains__('@'):
        temp += 1
    if temp == 3:
        allDone = createAccount(email, password)
    else:
        return False

    return allDone

def createAccount(email, password):
    user = users.find_one({"email":email})
    if user == None:
        db.users.insert_one({"email":email, "password":Encryptor.Encrypt(password)})
        db.credentials.insert_one({'email':email, 'passwords':{}})
        return True
    else:
        return False

def Details(email):
    # Returning Key Count
    try:
        usercredentials = credentials.find_one({"email":email})
        passwords = usercredentials["passwords"]
        keyCount = len(passwords.keys())
        keyList = []
        for key, value in passwords.items():
            keyList.append(key)

    except:
        keyCount = 0
        keyList = []

    return keyCount, keyList

def getPass(objectName, email):
    usercredentials = credentials.find_one({"email":email})
    passwords = usercredentials["passwords"]
    password = passwords[f"{objectName}"]

    return Encryptor.Decrypt(password)

def createPassword(Name, Characters, Capital, Small, Numbers, Symbols, email):
    usercredentials = credentials.find_one({"email":email})
    passwords = usercredentials["passwords"]
    password = RPG.generateNewPassword(Characters, Capital, Small, Numbers, Symbols)
    if password != False:
        passwords[f"{Name}"] = Encryptor.Encrypt(password)
        db.credentials.update_one({"_id":usercredentials["_id"]}, {"$set":{"passwords":passwords}})
    else:
        return False
    
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
    if password == Encryptor.Decrypt(dbpassword):
        db.users.delete_one({"_id":user["_id"]})
        db.credentials.delete_one({"email":email})
        return True
    else:
        return False