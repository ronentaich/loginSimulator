# This program displays a simple login system 
import random
import re
import getpass
# import string
# import sys


class Login:
    def __init__(self):
        self._firstName = ""  # the first name the user enters when registering
        self._lastName = ""  # the last name the user enters when registering
        self._emailAddress = ""  # the email address the user enters when registering
        self._userName = ""  # the username the user enters when registering
        self._passWord = ""  # password that is entered corresponding to the username and email
        self._userNameLogin = ""  # username the user enters when they log in (option B)
        self._passWordLogin = ""  # password the user enters when they log in (option B)
        self._userDict = {}  # username:password
        self._emailDict = {}  # email:password
        self._emailDict2 = {}  # email:username

    def displayMenu(self):
        print("Welcome to the Login Project!")
        print("=============================")
        print("A: Create a new account")
        print("B: Login to your account")
        print("C: Forgot username/password")
        print("D: Quit")
        print("=============================")

    def getInputs(self):

        flagOverview = True

        while flagOverview:

            flagPassword = True
            flagLogin = True
            flagUsername = True
            flagFile = False
            flagName = True
            flagEmail = True

            userInput = input("Please select one of the options.")
            userInput = userInput.upper()

            if userInput == 'A':
                self._firstName = input("Enter your first name:")

                self._lastName = input("Enter your last name:")

                while flagEmail:
                    self._emailAddress = input("Enter your email address:")
                    if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',self._emailAddress)):
                        flagEmail = False
                    else:
                        print("You must provide a valid email.")


                print(
                    "Please enter a username. It must be at least 7 characters long.")
                print("Suggested usernames: ")
                number = '{:03d}'.format(random.randrange(1, 999))
                number2 = '{:03d}'.format(random.randrange(1, 999))
                number3 = '{:03d}'.format(random.randrange(1, 999))

                s = self._firstName + number
                w = self._lastName + number2
                z = self._firstName + self._lastName + number3

                print(s)
                print(w)
                print(z)

                while flagUsername:

                    self._userName = input("Username:")

                    letterCount = 0

                    if (self._userName in self._userDict):
                        print("This username is taken. Please re-enter.")

                    else:
                        for letter in self._userName:
                            letterCount = letterCount + 1

                        if letterCount >= 7:
                            print("Your username is valid.")
                            flagUsername = False

                        elif self._userName == 'Q':
                            flagUserName = False
                            flagPassword = False

                        else:
                            print("Your username is invalid.")

                while flagPassword:
                    print(
                        "Your password must contain at least 8 characters and have a capital letter and a '$' symbol in it:")
                    self._passWord = getpass.getpass("Password:")
                    passWord2 = getpass.getpass("Please re-enter your password:")
                    pLetterCount = 0

                    for letter in self._passWord:
                        pLetterCount = pLetterCount + 1

                    if pLetterCount > 8 and any(x.isupper() for x in
                                                self._passWord) and self._passWord == passWord2 and '$' in self._passWord:
                        self._userDict[self._userName] = self._passWord
                        self._emailDict[self._emailAddress] = self._passWord
                        self._emailDict2[self._emailAddress] = self._userName
                        print("Your password is valid")
                        flagPassword = False
                        flagFile = True

                    else:
                        print("Invalid password.")

                    while flagFile:
                        fileName = self._userName + "_info.txt"

                        with open(fileName, "w") as f:
                            f.write("First Name: ")
                            f.write(self._firstName)
                            f.write("\n")
                            f.write("Last Name: ")
                            f.write(self._lastName)
                            f.write("\n")
                            f.write("Email Address: ")
                            f.write(self._emailAddress)
                            f.write("\n")
                            f.write("Username: ")
                            f.write(self._userName)
                            f.write("\n")
                            f.write("Password: ")
                            f.write(self._passWord)

                        print("Your account has been created! You can see your information at the", fileName, "file.")
                        flagPassword = False
                        flagFile = False


            elif userInput == 'B':

                while flagLogin:
                    self._userNameLogin = input("Please enter your username (or Q to quit):")

                    if self._userNameLogin == 'Q':
                        break

                    self._passwordLogin = getpass.getpass("Please enter your password:")

                    if self._userNameLogin in self._userDict and self._passwordLogin == self._userDict[
                        self._userNameLogin]:
                        print("You have logged in!")
                        flagLogin = False

                    else:
                        print("Either your username or password is incorrect. Please try again or press Q to quit.")


            elif userInput == 'C':
                flagEmailRepeat = True
                print("In order to retrieve your username and password, please enter your email or enter 'Q' to quit:")
                while flagEmailRepeat:
                    emailEntry = input("Email:")
                    if emailEntry in self._emailDict:
                        print("Your username is", self._emailDict2[emailEntry])
                        print("Your password is", self._emailDict[emailEntry])
                        flagEmailRepeat = False

                    elif emailEntry == 'Q' or emailEntry == 'q':
                        flagEmailRepeat = False

                    else:
                        print("We do not have that email in our system. Please re-enter or press Q to quit.")


            elif userInput == 'D':

                print("======================================")
                print("Thank you for using the Login Program!")
                print("======================================")
                flagOverview = False

            else:
                print("Please select one of the given options in the menu")
