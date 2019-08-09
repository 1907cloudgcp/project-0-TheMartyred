import sys
sys.path.append("../../../../")
from main.controller import BankingController
from main.services import DataAccess

def main():
    testAuthentication()

def testAuthentication():
    # creates a set of data to test on
    data = [{"username" : "blake", "password" : "password1", "balance" : -30000, "transactions" : [("w", 200), ("d", -3)]}, {"username" : "roniel", "password" : "12340", "balance" : 666, "transactions" : [("jjsjs", 5), ("ffff", 0)]}]
    # sends that data to be written
    DataAccess.writeData(data)
    

    
