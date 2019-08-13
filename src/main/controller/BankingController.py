import main.services.DataAccess as DataAccess
import main.error.CustomErrors as errors
import logging

class BankingController():

    def __init__(self):
        self.data = DataAccess.readData()
        self.logger = logging.getLogger("logging")
        logging.basicConfig(level = "DEBUG", filename = "test/logs/log.txt")
        self.logger.info("Program started")

    def createUser(self, username, password, startingBalance = 0):
        if startingBalance == "":
            startingBalance = 0
        valid = True
        #make sure it does not contain reserved characters used as delimiters
        if not username.isalnum():
            valid = False
            self.logger.error("Username: '"+username+"' is not alphanumeric and is therefore invalid")
        if password.find(";") > -1 or password.find(":") > -1 or password.find(",") > -1:
            self.logger.error("Password: '"+password+"' contains reserved delimiter characters and is therefore invalid")
            raise errors.InvalidPasswordError("Password contains reserved delimiter characters.")
        for user in self.data:
            if username == user["username"]:
                self.logger.error("The username, '"+username+"' entered was found in the existing list of users and is therefore invalid")
                valid = False
        if valid:
            self.data.append({"username": username, "password": password, "balance": startingBalance, "transactions": []})
            self.refresh()
            self.logger.info("User, "+username+" successfully added")
        return valid

    def validateUser(self, username, password):
        for user in self.data:
            if username == user["username"] and password == user["password"]:
                self.logger.info("User, "+username+" has successfully logged in.")
                return True
        self.logger.warning("Detected failed log in attempt for username, "+username+"!")
        return False

    def getBalance(self, username):
        for user in self.data:
            if user["username"] == username:
                self.logger.info("User, "+username+" showing balance of $"+str(user["balance"]))
                return user["balance"]

    def deposit(self, username, amount):
        amount = self.validateAmount(amount)
        for user in self.data:
            if user["username"] == username:
                user["balance"] += amount
                user["transactions"].append(("d",amount))
                self.logger.info("User, "+username+" deposited $"+str(amount))
        self.refresh()

    def withdraw(self, username, amount):
        amount = self.validateAmount(amount)
        for user in self.data:
            if user["username"] == username:
                user["balance"] -= amount
                if user["balance"] < 0:
                    self.logger.error("withdrawing $"+str(amount)+" from "+username+" would result in a balance of "+str(user["balance"])+"! Transaction cancelled.")
                    user["balance"] += amount
                    raise errors.NegativeBalanceError("Transaction would have made user balance negative")
                user["transactions"].append(("w",amount))
                self.logger.info("Amount withdrawn from "+username+": "+str(amount))
        self.refresh()

    def validateAmount(self, amount):
        """checks to ensure that the amount is a valid non-negative dollar amount"""
        try:
            amount = float(amount)
            if str(amount)[::-1].find(".") > 2 or amount < 0:
                self.logger.error("Input not a valid dollar amount")
                raise errors.InvalidMoneyError("The input provided was invalid.")
        except ValueError:
            self.logger.error("Input not a valid number")
            raise errors.InvalidMoneyError("The input provided was not a number")
        return amount

    def viewHistory(self, username):
        for user in self.data:
            if user["username"] == username:
                self.logger.info("User, "+username+" viewing transactions.")
                return user["transactions"]

    def refresh(self):
        DataAccess.writeData(self.data)
        self.data = DataAccess.readData()
