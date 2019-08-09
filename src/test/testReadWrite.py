import sys
sys.path.append("../../../../")
from main.services import DataAccess

def main():
    #create data for testing
    data = [{"username" : "blake", "password" : "password1", "balance" : -30000, "transactions" : [("w", 200), ("d", -3)]}, {"username" : "roniel", "password" : "12340", "balance" : 666, "transactions" : [("jjsjs", 5), ("ffff", 0)]}]
    #test the write function
    DataAccess.writeData(data)
    #reset data so that we can be sure it is not just remaining in the variable
    data = "didn't work"
    
    assert(data == "didn't work")
    #read the data back from the file
    data = DataAccess.readData()
    #check to make sure we recieved the same data back
    assert(data == [{"username" : "blake", "password" : "password1", "balance" : -30000, "transactions" : [("w", 200), ("d", -3)]}, {"username" : "roniel", "password" : "12340", "balance" : 666, "transactions" : [("jjsjs", 5), ("ffff", 0)]}])

main()
