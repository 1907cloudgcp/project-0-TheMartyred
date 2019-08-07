def readData(filePath="main/resources/BankingInfo"):
    #create an empty data object to store the data we pull from the file
    data = []
    #open the file at the default or provided path
    with open(filePath, "r") as file:
        #read the entire file into a variable
        textData = file.read()
        #parse through that variable, seperating users
        delimiter = ":"
        userData = textData.split(delimiter)
        #try:
        #go through each user and parse out the necessary data into dicts
        for user in userData:
            #first, separate the pieces of data into a list by delimiter
            delimiter = ";"
            dataMembers = user.split(delimiter)
            #print(dataMembers)
            if len(dataMembers) < 4:
                break
            #get the username, password and balance from this
            userInfo = {}
            userInfo["username"] = dataMembers[0]
            userInfo["password"] = dataMembers[1]
            userInfo["balance"] = float(dataMembers[2])
            #next, parse out the information on transactions
            userInfo["transactions"] = []
            for transaction in dataMembers[3:]:
                #check to make sure its not the last transaction
                if len(transaction) < 2:
                    break
                #create a tuple with the first member being the type and the second being the amount
                delimiter = ","
                transactionInfo = transaction.split(delimiter)
                userInfo["transactions"].append((transactionInfo[0], float(transactionInfo[1])))
            #add this user to the data
            data.append(userInfo)
##        except:
##            #raise DataAccessError("Problem parsing data. Check that it's formatted correctly.")
##            print("Failed to read")
##            pass
##        finally:
##            print(data)
    return data

def writeData(data, filePath="/main/resources/BankingInfo"):
    #instantiate a string to add to
    textData = ""
    #iterate through users and construct a string to save to file
    for user in data:
        #for each user, iterate through their transactions and construct that portion of the string
        transactions = ""
        for transaction in user["transactions"]:
            transactions += transaction[0] + "," + str(transaction[1]) + ";"
        #construct the string representing the rest of this user's information
        textData += user["username"] + ";" + user["password"] + ";" + str(user["balance"]) + ";" + transactions + ":"
    #open a file to write
    with open(filePath, "w") as file:
        #write the data in text form with its delimiters
        #print(textData)
        file.write(textData)
