import time
import json
import random


# Read In Login Information Into Game
def readUserData():
    with open("Login_Users_Information") as login:
        content = str(login.readlines())
        return content


# User creates new profile
def createNewProfile(newUsername, newPassword, filename):
    with open(filename, "a") as setLogin:
        setLogin.write(newUsername + "\n")
        setLogin.write(newPassword + "\n")


# Access a profile
def accessNewProfile(username, password):
    profiles = readUserData()
    if username in profiles and password in profiles:
        return True

# Save the highest score of the player (highest level they go to)
def saveHighestScore(nString, filename="User_Scores"):
    with open(filename, "a") as saveScore:
        saveScore.write(nString)

# Write to file the current player
def saveCurrentUser(player3, filename="Current_User"):
    with open(filename, "w") as savePlayer:
        savePlayer.write(player3)

# Save data for the replay information
def replayGameData(block, level, filename="Replay_Data"):
    with open(filename, "a") as replayInformation:
        currentTime = time.ctime()
        gameInformation = "LAST MOVE: " + str(block) + " Current Level: " + str(level) + " Timestamp: " + str(
            currentTime)
        replayInformation.write(gameInformation + "\n")

# Save specific block that was selected by player last
def saveSelectedBlock(block, filename="Replay_Data"):
    with open(filename, "a") as replayInformation:
        currentTime = time.ctime()
        gameInformation = "BLOCK: " + str(block) + " Timestamp: " + str(currentTime)
        replayInformation.write(gameInformation + "\n")

# Save the replay information, starting with the player's name
def saveUserToReplay(user, filename="Replay_Data"):
    with open(filename, "a") as replayInformation:
        player = "\nPLAYER USER: " + user + "\n"
        replayInformation.write(player)

# Save the replay information, starting with the player's name (invalid)
def saveUserScoreFile(userName, filename):
    with open(filename, "a") as replayInformation:
        player = "\nPLAYER USER: " + userName + "\n"
        replayInformation.write(player)

# get the scores from score file (not used)
def getScores(filename="User_Scores"):
    file = open("User_Scores", "r")

    for line in file:
        fields = line.split(",")

        userName = fields[0]
        score = fields[1]

        print(userName + " with " + score)

    file.close()

# sorts the scores of the users, encryption is used in the other function
def sortScores():
    with open("User_Scores") as f:
        scores = [(name, int(score)) for name, score in (line.split(',') for line in f)]
        scores.sort(key=lambda s: s[1])
        scores.reverse()
        f.close()
        with open("User_Scores", 'w') as f2:
            for name, score in scores:
                '''
                encrypted = moreEncryption(str(name), random.randint(0,20))
                f2.write(str(encrypted) + ',' + str(score) + '\n')
                '''
                f2.write(str(name) + ',' + str(score) + '\n')

# End
