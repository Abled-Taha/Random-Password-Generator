import string
import random

def generateNewPassword(Characters, Capital, Small, Numbers, Symbols):
    if Capital == True or Small == True or Numbers == True or Symbols == True:
        if Characters > 0:
            field = ""
            Password = ""
            if Capital:
                field += string.ascii_uppercase
            if Small:
                field += string.ascii_lowercase
            if Numbers:
                field += string.digits
            if Symbols:
                field += string.punctuation
            
            while Characters > 0:
                temp = random.choice(field)
                Password += temp
                Characters -= 1
        else:
            return False

    else:
        return False

    return Password