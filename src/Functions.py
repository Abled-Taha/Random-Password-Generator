import os
import json
import Encryptor
import RandomPasswordGenerator as RPG

def validateSignIn(username, password):
    if os.path.isfile(f"Files/Accounts/{username}.json"):
        encryptedPassword = Encryptor.Encrypt(password)
        os.chdir("Files/Accounts")
        with open(f"{username}.json") as File:
            data = json.load(File)
        os.chdir("../..")
    else:
        return False
    if data["MainPassword"] == encryptedPassword:
           return True
    else:
        return False

def validateSignUp(username, password, confirmPassword):
    if password == confirmPassword:
        pass
    if username != "":
        pass
    else:
        return False
    allDone = createAccount(username, password)

    return allDone

def createAccount(username, password):
    if os.path.isdir("Files/Accounts"):
        if os.path.isfile(f"Files/Accounts/{username}.json"):
            return False
    else:
        os.mkdir("Files/Accounts")

    encryptedPassword = Encryptor.Encrypt(password)
    os.chdir("Files/Accounts")
    dict = {"MainPassword" : f"{encryptedPassword}"}
    jsonObj = json.dumps(dict, indent=1)
    with open(f"{username}.json", "a+") as File:
        File.write(jsonObj)
    os.chdir("../..")
    return True

def Details(username):
    # Returning Key Count
    os.chdir("Files/Accounts")
    with open(f"{username}.json") as File:
        data = json.load(File)
    keyCount = len(data.keys())
    keyCount -= 1
    os.chdir("../..")

    # Returning Password Name
    os.chdir("Files/Accounts")
    with open(f"{username}.json") as File:
        data = json.load(File)
    keyList = []
    for key, value in data.items():
        keyList.append(key)
    keyList.pop(0)
    os.chdir("../..")

    return keyCount, keyList

def getPass(objectName, username):
    os.chdir("Files/Accounts")
    with open(f"{username}.json") as File:
        data = json.load(File)
    EncryptedPassword = data[f"{objectName}"]
    DecryptedPassword = Encryptor.Decrypt(EncryptedPassword)
    os.chdir("../..")

    return DecryptedPassword

def createPassword(Name, Characters, Capital, Small, Numbers, Symbols, username):
    Password = RPG.generateNewPassword(Characters, Capital, Small, Numbers, Symbols)
    if Password != False:
        EncryptedPassword = Encryptor.Encrypt(Password)
        os.chdir("Files/Accounts")

        with open(f"{username}.json") as File:
            data = json.load(File)
        data[f"{Name}"] = EncryptedPassword
        os.remove(f"{username}.json")

        with open(f"{username}.json", "a+") as File:
            json.dump(data, File)
        os.chdir("../..")
        return True
    else:
        return False

def deletePassword(Name, username):
    os.chdir("Files/Accounts")

    with open(f"{username}.json") as File:
        data = json.load(File)
    try:
        del data[f"{Name}"]
    except:
        os.chdir("../..")
        return False
    os.remove(f"{username}.json")

    with open(f"{username}.json", "a+") as File:
        json.dump(data, File)
    os.chdir("../..")

    return True

def deleteUser(username, password):
    if os.path.isfile(f"Files/Accounts/{username}.json"):
        encryptedPassword = Encryptor.Encrypt(password)
        os.chdir("Files/Accounts")
        with open(f"{username}.json") as File:
            data = json.load(File)
        os.chdir("../..")
    else:
        return False
    if data["MainPassword"] == encryptedPassword:
        os.chdir("Files/Accounts")
        os.remove(f"{username}.json")
        os.chdir("../..")
        return True
    else:
        return False