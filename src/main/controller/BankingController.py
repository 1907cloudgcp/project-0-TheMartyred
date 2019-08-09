import main.services.DataAccess as DataAccess
import main.error.CustomErrors as errors

class BankingController():

    def __init__(self):
        self.data = DataAccess.readData()

    def createUser(self, username, password, startingBalance = 0):
        if startingBalance == "":
            startingBalance = 0
        valid = True
        for user in self.data:
            if username == user["username"]:
                valid = False
        if valid:
            self.data.append({"username": username, "password": password, "balance": startingBalance, "transactions": []})
            self.refresh()
        return valid

    def validateUser(self, username, password):
        for user in self.data:
            if username == user["username"] and password == user["password"]:
                return True
        return False

    def getBalance(self, username):
        for user in self.data:
            if user["username"] == username:
                return user["balance"]

    def deposit(self, username, amount):
        amount = self.validateAmount(amount)
        for user in self.data:
            if user["username"] == username:
                user["balance"] += amount
                user["transactions"].append(("d",amount))
        self.refresh()

    def withdraw(self, username, amount):
        amount = self.validateAmount(amount)
        for user in self.data:
            if user["username"] == username:
                user["balance"] -= amount
                user["transactions"].append(("w",amount))
        self.refresh()

    def validateAmount(self, amount):
        """checks to ensure that the amount is a valid non-negative dollar amount"""
        try:
            amount = float(amount)
            if str(amount)[::-1].find(".") > 2 or amount < 0:
                raise errors.InvalidMoneyError("The input provided was invalid.")
        except ValueError:
            raise errors.InvalidMoneyError("The input provided was not a number")
        return amount

    def viewHistory(self, username):
        for user in self.data:
            if user["username"] == username:
                return user["transactions"]

    def refresh(self):
        DataAccess.writeData(self.data)
        self.data = DataAccess.readData()
