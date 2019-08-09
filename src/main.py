import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import main.controller.BankingController as BC

'''
This is your main script, this should call several other scripts within your packages.
'''
def main():
        #set basic variables
        username = ""
        selection = ""
        #loop until the user chooses to end the program
        while selection != "0":
                #if they are logged in, print their information
                if username:
                        print("Hello, "+username)
                print("Welcome to Revature Banking!\nPlease select one of the options below:\n0) Quit\n1) Create New User\n2) Log in New User")
                #if they are logged in, add more options
                if username:
                        print("3) Logout "+username+"\n4) View Balance\n5) Withdraw\n6) Deposit\n7) View Transaction History")
                selection = input()
                if selection == 1:
                        #ask for username and password from user
                        print("Enter a username (must be unique):")
                        username = input()
                        print("Enter a password:")
                        password = input()
                        #loop until successful
                        while not BC.createUser(username, password, starting balance) and username != "quit":
                                #if the creation failed, ask for a different username
                                print(username+" is already taken. Try something else:")
                                username = input()
                        if username == "quit":
                                #if the user quit the creation without finishing, ensure that username goes back to empty
                                username = ""
                                print("User Creation Cancelled...")
                        else:
                                print("User Creation Successful")
                elif selection == 2:
                        username = login()
                elif selection == 3 and username:
                        #logout by just setting username back to empty
                        username = ""
                elif selection == 4 and username:
                        print("Your Balance: "+str(BC.getBalance(username))
                elif selection == 5 and username:
                        withdraw()
                elif selection == 6 and username:
                        deposit()
                elif selection == 7 and username:
                        viewHistory()

def login():
        '''asks for input and returns username if login was
successful and the empty string if it failed'''
        print("Please enter your username:")
        username = input()
        print("Please enter your password:")
        password = input()
        if BC.validateUser(username, password):
                print("Login Successful!")
                return username
        print("Login Failed!")
        return ""
                
if __name__ == '__main__':
	main()
