import sys
sys.path.append("../../../../")
from main.controller import BankingController
from main.services import DataAccess

path = "main/resources/testData"

def main():
    testAuthentication()
    testCreate()

def testAuthentication():
    # creates a set of data to test on
    data = [{"username" : "blake", "password" : "password1", "balance" : -30000, "transactions" : [("w", 200), ("d", -3)]}, {"username" : "roniel", "password" : "12340", "balance" : 666, "transactions" : [("jjsjs", 5), ("ffff", 0)]}]
    # sends that data to be written
    DataAccess.writeData(data, path)
    BC = BankingController.BankingController()
    assert(BC.validateUser("blake", "passwo") == False)
    assert(BC.validateUser("blake", "password") == True)
    assert(BC.validateUser("bake", "password") == False)

def testCreate():
    # creates a set of data to test on
    data = [{"username" : "blake", "password" : "password1", "balance" : -30000, "transactions" : [("w", 200), ("d", -3)]}, {"username" : "roniel", "password" : "12340", "balance" : 666, "transactions" : [("jjsjs", 5), ("ffff", 0)]}]
    # sends that data to be written
    DataAccess.writeData(data, path)
    BC = BankingController.BankingController()
    assert(BC.createUser("blake", "password") == False)
    assert(BC.createUser("bla-", "password") == False)
    try:
        assert(BC.createUser("bla;", "password") == False)
    except Exception as error:
        print(error)
    try:
        assert(BC.createUser("blake", "pass;ord") == False)
    except Exception as error:
        print(error)
