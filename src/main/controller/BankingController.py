import main.services.DataAccess as DataAccess

data = DataAccess.readData()

def createUser(username, password, startingBalance = 0):
    if startingBalance == "":
        startingBalance = 0
    valid = True
    for user in data:
        if username == user["username"]:
            valid = False
    if valid:
        data.append({"username": username, "password": password, "balance": startingBalance, "transactions": []})
        refresh()
    return valid

def validateUser(username, password):
    for user in data:
        if username == user["username"] and password == user["password"]:
            return True
    return False

def getBalance(username):
    for user in data:
        if user["username"] == username:
            return user["balance"]

def refresh():
    DataAccess.writeData(data)
    data = DataAccess.readData()
