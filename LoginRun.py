'''
Tyler Bramlett
CS 3160
Final Project
Corsi Study
Due: 18 DEC 19

LoginRun.py
This file will run all the Tkinter module stuff for the login and signup screen(s)
'''

# Import statements
from tkinter import *
import time
import os
import tkinter.messagebox as tm
from InputOutput import *
from Test import *

# Create a class for the popup window
class WindowLoginPopup(Frame):
    # Constructor
    def __init__(self, master):
        super().__init__(master)
        # Main title, created from a label
        headerTitle1 = Label(master, text="LOGIN TO PLAY", font=("Helvetica", 30), padx=40, pady=40)
        headerTitle1.pack()
        # Set up all entries and buttons displayed on windows
        self.entryboxForUser = Label(self, text="Username:", padx=20)
        self.entryboxForPassw = Label(self, text="Password:", padx=20)
        self.enteredName = Entry(self)
        self.enteredPassw = Entry(self, show="*")
        self.entryboxForUser.grid(row=0, sticky=E)
        self.entryboxForPassw.grid(row=1, sticky=E)
        self.enteredName.grid(row=0, column=1)
        self.enteredPassw.grid(row=1, column=1)
        self.button_PlayGame = Button(self, text="Login and Play Game", command=self.startgame, padx=30)
        self.button_PlayGame.grid(columnspan=2, pady=10)
        self.button_createProfile = Button(self, text="Create Profile", command=self.signupWindow, padx=30, )
        self.button_createProfile.grid(columnspan=2, pady=10)
        # Pack everything and add padding to the y axis
        self.pack(pady=10)

    def signupWindow(self):
        # New instance
        newWindow = Toplevel()
        # Title name
        newWindow.title('Signup')
        # Setup all items on window
        self.windowSignup = Label(newWindow, text="SIGNUP", font=("Helvetica", 30))
        self.newUserName = Label(newWindow, text="Create a Username:")
        self.signupPassword = Label(newWindow, text="Create a Password:")
        self.comp_signupPassword = Label(newWindow, text="Re-Enter Password:")
        self.windowSignup.grid(row=0, column=1)
        self.signupEntryName = Entry(newWindow)
        self.signupEntryPassw = Entry(newWindow, show="*")
        self.signupEntryPassw_comp = Entry(newWindow, show="*")
        self.newUserName.grid(row=1, sticky=E)
        self.signupPassword.grid(row=2, sticky=E)
        self.comp_signupPassword.grid(row=3, sticky=E)
        self.signupEntryName.grid(row=1, column=2)
        self.signupEntryPassw.grid(row=2, column=2)
        self.signupEntryPassw_comp.grid(row=3, column=2)
        # Button to save enter new window
        button_signup = Button(newWindow, text="Create Account", command=self.createaccountandpassword, padx=30)
        button_signup.grid(column=1, pady=10)

    # Create account password and username window for signup
    def createaccountandpassword(self):
        validUsername = self.signupEntryName.get()
        validPassword = self.signupEntryPassw.get()
        validPassword_comp = self.signupEntryPassw_comp.get()

        # Check to see if the passwords are the same, and then continue to prev window
        if validUsername and validPassword is not None:
            if validPassword == validPassword_comp:
                createNewProfile(validUsername, validPassword, "Login_Users_Information")
                tm.showinfo("Signup Successful", "New Account Created! Your Signup was successful")
            else:
                # Error
                tm.showinfo("Ooops", "Your Passwords do not match!")

        else:
            # Invalid credentials
            tm.showerror("Signup ERROR", "Invalid Credentials")

    # Finish the login and prepare for the game to begin
    def startgame(self):
        sName = self.enteredName.get()
        sPassw = self.enteredPassw.get()

        # Check for the passwords to correct
        if sName and sPassw is not None:
            isValidLogin = accessNewProfile(sName, sPassw)
            # Check login, thus decrypt and then save data
            if isValidLogin:
                decryptScores()
                saveHighestScore(sName)
                savePlayer(sName, "Current_User")
                saveUserToReplay(sName)
                tm.showinfo("Login Successful", "Welcome To the Corsi Study!")
            else:
                tm.showerror("Login ERROR",
                             "Incorrect username or password. Please re-enter your username and password!")
        else:
            tm.showerror("Login ERROR", "No Username or password detected!")

# Tkinter module stuff
root = Tk()
runLogin = WindowLoginPopup(root)
root.mainloop()
