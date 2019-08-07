import sys
sys.path.append("../../../../")
from main.python.com.revature.service import DataAccess

data = [{"username" : "blake", "password" : "password1", "balance" : -30000, "transactions" : [("w", 200), ("d", -3)]}, {"username" : "roniel", "password" : "12340", "balance" : 666, "transactions" : [("jjsjs", 5), ("ffff", 0)]}]

print(data)

DataAccess.writeData(data)

data = "didn't work"

data = DataAccess.readData()

print(data)
