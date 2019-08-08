import main.services.DataAccess as DataAccess

data = DataAccess.readData()

def validateUser(username, password):
    for user in data:
        if username == user["username"] and password == user["password"]:
            return True
    return False
