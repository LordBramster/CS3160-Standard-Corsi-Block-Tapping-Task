import random
import re
from collections import Counter

# The char list
alphabetKey = 'abcdefghijklmnopqrstuvwxyz'

# Encrypt all the scores when called
def encryptScores(filename="User_Scores"):
    with open(filename) as f:
        importedFileLines = [(importedUser, int(num)) for importedUser, num in (line.split(',') for line in f)]
        importedFileLines.sort(key=lambda s: s[1])
        importedFileLines.reverse()
        f.close()
        with open("User_Scores", 'w') as f2:
            for importedUser, num in importedFileLines:
                encrypted = encrypt(4, str(importedUser))
                f2.write(str(encrypted) + ',' + str(num) + '\n')
        f.close()

# Encrypt any given string based on ceaser cipher
def encrypt(shift, string):
    encryptedLine = ''

    for char in string.lower():
        i = (alphabetKey.index(char) + shift) % 26
        encryptedLine += alphabetKey[i]

    return encryptedLine.lower()

# decrypt any given string with ceaser cipher
def decrypt(shiftback, encryptedstring):
    decryptedline = ''

    for char in encryptedstring:
        i = (alphabetKey.index(char) - shiftback) % 26
        decryptedline += alphabetKey[i]

    return decryptedline

# decrypt the score file as a whole
def decryptScores(filename="User_Scores2"):
    allScores = []
    with open("User_Scores") as file:
        for line in file:
            user, scorenum = line.split(',')
            scorenum = int(scorenum)
            allScores.append((user, scorenum))
    file.close()
    # sort them
    allScores.sort(key=lambda x: x[1])
    allScores.reverse()

    with open("User_Scores", 'w') as file2:
        for user, scorenum in allScores:
            decrypted = decrypt(4, str(user))
            file2.write(str(decrypted) + ',' + str(scorenum) + '\n')
    file2.close()

# Sort the personal leaderboard scores
def sortPersonalScores(user, filename="User_Scores"):
    user = user.lower()
    print("CURRENT PLAYER: " + user)
    with open(filename) as f:
        importedFileLines = [(importedUser, int(num)) for importedUser, num in (line.split(',') for line in f)]
        importedFileLines.sort(key=lambda y: y[1])
        importedFileLines.reverse()
        for element in importedFileLines:
            if user in element:
                print("Player: " + element[0] + " Score: " + str(element[1]))
        f.close()

# decrypt who the current player is
def findPlayer(filename="Current_User"):
    with open(filename) as f:
        userName2 = f.readline()
        decrypted = decrypt(4, userName2)
        f.close()
    return decrypted

# Save any given player name and encrypt it
def savePlayer(playerName="Unknown_Player", filename="Current_User"):
    with open(filename, 'w') as f:
        encrypted = encrypt(4, playerName)
        f.write(str(encrypted))
        f.close()

# TEST FUNCTION, ignored
def basicScores():
    importedFileLines = []
    with open("User_Scores2") as f:
        for line in f:
            player, num = line.split(',')
            num = int(num)
            importedFileLines.append((player, num))

    importedFileLines.sort(key=lambda s: s[1])
    importedFileLines.reverse()
    print(importedFileLines)

# sort the scores of all players and find just the scores of the current player
def sortPersonalScores2(user, filename="User_Scores"):
    user = user.lower()
    print("CURRENT PLAYER: " + user)
    importedFileLines = []
    with open("User_Scores2") as f:
        for line in f:
            player, num = line.split(',')
            num = int(num)
            importedFileLines.append((player, num))

    importedFileLines.sort(key=lambda s: s[1])
    importedFileLines.reverse()
    for element in importedFileLines:
        if user in element:
            print("Player: " + element[0] + " Score: " + str(element[1]))
    f.close()

# Encrypt multiple files, such as the login data
def encryptFiles(filename="Login_Users_Information"):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
        with open("Login_Users_Information2", 'w') as f2:
            for line in lines:
                # encrypted = encrypt(random.randint(0, 25), str(line))
                f2.write(str(encrypt(5, str(line))))
        f.close()

# commented out method calls to prevent functions running on accident
#encryptScores()
#decryptScores()
#encryptFiles()
