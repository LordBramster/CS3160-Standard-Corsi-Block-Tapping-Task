# All of my input statements, including the ones that refer to my other files
import pygame
import time
import random
import os
import LoginRun
from InputOutput import *
from Test import *

# Create a Block class
class Block:
    # Constructor
    def __init__(self, blockColor, highlightColor, pixelPosition):
        # This is the block's RGB color
        self.blockColor = blockColor
        # This is the block's new RGB color for when it is highlighted onscreen
        self.highlightColor = highlightColor
        # Setup new block, with rectangle shape at the pixel position
        self.rect = pygame.Rect(pixelPosition)
        # Call function, and pass the block's RGB color
        self.displayRect(screen, self.blockColor)

    # Function will create a rectangle onto the screen
    def displayRect(self, screen, colorRGB):
        # Draw the actual rectangle, which shall be used by each block
        pygame.draw.rect(screen, colorRGB, self.rect)
        pygame.display.update()

    # Function will highlight the current block to be followed
    def highlightBlock(self, screen):
        self.displayRect(screen, self.highlightColor)
        # Sleep to create a delay between the highlighting
        time.sleep(0.7)
        self.displayRect(screen, self.blockColor)


# Hide the selected area
def hideArea():
    # Use RGB = (0,0,0) to represent the black background of the boards
    blackBackground = (0, 0, 0)
    # Draw this cover over the position needed
    # I used this to cover the center text that displays, to cover over the previous text
    pygame.draw.rect(screen, blackBackground, (halfWidth - 125, halfHeight, 250, 30))


# Any message sent to the screen,
def displayMessage(onScreen, string, font, pixelsX, pixelsY):
    # Render the font
    rect1 = font.render(string, True, (255, 255, 255)).get_rect()
    rect1.midtop = (pixelsX, pixelsY)
    onScreen.blit(font.render(string, True, (255, 255, 255)), rect1)

# Selects the button at a location under mouse cursor
def selectButton(blockList, mouseCursor):
    # For all blocks on screen, if the mouse cursor clicks on it, then return that one
    for onScreenRect in blockList:
        if onScreenRect.rect.collidepoint(mouseCursor):
            return onScreenRect
    # Create default return:
    return None


# MAIN METHOD BEGINS:

# Run LoginRun separately, first, to popup the signup and login windows
os.system("LoginRun")

# Testing purposes only, thus ignored
currPlayer = "test_user"
print("Testcase:" + currPlayer)

# Initialize pygame
pygame.init()

# Create dimension variables
dimensionx = 800
dimensiony = 600
# Set the frame time to 30
frameTime = 30
# Create two variables for the mid point of both the x and y of the screen
halfWidth = (dimensionx / 2)
halfHeight = (dimensiony / 2)

# Set the screen size to the dimensions
screen = pygame.display.set_mode((dimensionx, dimensiony))
# I set the window caption to Corsi Study
pygame.display.set_caption('Corsi Study')
frame = pygame.time.Clock()

# Create large font
LargeFont = pygame.font.Font(pygame.font.match_font('Comic Sans MS'), 60)
# Create small font
SmallerFont = pygame.font.Font(pygame.font.match_font('Comic Sans MS'), 20)
# Create a list of blocks, that will be added in sequence
sequenceBlocks = []
# Set phases of pygame to True, so they can be run
mainGameStart = True
personal_scoreboard = True
leader_board = True
setupBlocks = True

# Set block size and set the instantiation of others to 0
userBlockScore = 0
currBlock = 0
blockSize = 100
blockType = 3

# Blue Block random position
posx1 = random.choice([20, 592, 143])
if posx1 is 20:
    posy1 = 19
elif posx1 is 592:
    posy1 = 32
else:
    posy1 = 400

# Red Block random position
posx2 = random.choice([28, 368, 658])
if posx2 is 28:
    posy2 = 478
elif posx2 is 368:
    posy2 = 104
else:
    posy2 = 268

# Yellow Block random position
posx3 = random.choice([278, 258, 662])
if posx3 is 258:
    posy3 = 12
elif posx3 is 278:
    posy3 = 468
else:
    posy3 = 149

# Green Block random position
posx4 = random.choice([137, 319])
if posx4 is 137:
    posy4 = 39
elif posx4 is 319:
    posy4 = 411

# Brown Block random position
posx5 = random.choice([22, 139, 542])
if posx5 is 22:
    posy5 = 365
elif posx5 is 139:
    posy5 = 170
else:
    posy5 = 148

# Purple Block random position
posx6 = random.choice([21, 446, 578])
if posx6 is 21:
    posy6 = 134
elif posx6 is 446:
    posy6 = 476
else:
    posy6 = 399

# Gray Block random position
posx7 = random.choice([153, 476])
if posx7 is 153:
    posy7 = 284
else:
    posy7 = 11

# Orange Block random position
posx8 = random.choice([32, 548])
if posx8 is 32:
    posy8 = 247
else:
    posy8 = 268

# Pink Block random position
posx9 = random.choice([432, 250])
if posx9 is 250:
    posy9 = 125
else:
    posy9 = 358

# Create list of all block objects
allBlocks = [

    Block(pygame.Color('red'), pygame.Color(220, 0, 0), (
        posx2, posy2, blockSize, blockSize)),
    Block(pygame.Color('green'), pygame.Color(0, 220, 0), (
        posx4, posx4, blockSize, blockSize)),
    Block(pygame.Color('blue'), pygame.Color(0, 0, 220), (
        posx1, posy1, blockSize, blockSize)),
    Block(pygame.Color('yellow'), pygame.Color(160, 160, 0), (
        posx3, posy3, blockSize, blockSize)),
    Block(pygame.Color('brown'), pygame.Color(82, 74, 62), (
        posx5, posy5, blockSize, blockSize)),
    Block(pygame.Color('purple'), pygame.Color(152, 58, 224), (
        posx6, posy6, blockSize, blockSize)),
    Block(pygame.Color('orange'), pygame.Color(255, 100, 10), (
        posx8, posy8, blockSize, blockSize)),
    Block(pygame.Color('pink'), pygame.Color(255, 100, 180), (
        posx9, posy9, blockSize, blockSize)),
    Block(pygame.Color('gray'), pygame.Color(127, 127, 127), (
        posx7, posy7, blockSize, blockSize)),

]

# Main game loop, and the entirety of the game's process
while mainGameStart is True:
    # check for all events in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # End phase of main game
            mainGameStart = False
            personal_scoreboard = False
        # if the mouse button is clicked, and it is not showing the sequence
        elif event.type is pygame.MOUSEBUTTONDOWN and not setupBlocks:
            # The correct block is equal to the index of the current block
            buttonInSequencce = sequenceBlocks[currBlock]
            pressedButton = selectButton(allBlocks, event.pos)
            # If no block is pressed at all, then break
            if pressedButton is None:
                break
            # If the correct block is pressed
            elif pressedButton == buttonInSequencce:
                # Highlight the pressed button
                pressedButton.highlightBlock(screen)
                # Save data, on which block is saved and the color of the block
                saveSelectedBlock(str(sequenceBlocks[currBlock]) + " Color: " + str(sequenceBlocks[currBlock].blockColor))
                currBlock += 1
                # If the user has selected all the correct blocks
                if currBlock == len(sequenceBlocks):
                    # Setup the new sequence of blocks
                    setupBlocks = True
                    userBlockScore += 1
                    print(userBlockScore)
                    # decryptuserBlockScores()
                    replayGameData(pressedButton, userBlockScore)
                    # encryptScores()
                    currBlock = 0
            # Quit, if the wrong putton has been pressed
            else:
                mainGameStart = False

    # if the event for setting up block is active, then start
    if setupBlocks:
        # Display text message in center of the screen:
        hideArea()
        displayMessage(screen, 'WATCH THESE BLOCKS', SmallerFont, halfWidth, halfHeight)
        pygame.display.update()

        # Tell the events that it won't continue setting up blocks
        setupBlocks = False
        time.sleep(.5)
        # Add to the sequence a new block on a random selection:
        sequenceBlocks.append(allBlocks[random.randint(0, blockType)])
        # Highlight each block in sequence
        for pressedButton in sequenceBlocks:
            pygame.event.pump()
            # Call function and show on screen
            pressedButton.highlightBlock(screen)
            # Sleep between each highlight
            time.sleep(0.2)

        # Cover over middle text, and display message
        hideArea()
        displayMessage(screen, 'IT IS YOUR TURN !', SmallerFont, halfWidth, halfHeight)
        pygame.display.update()

    # pygame limit to framerate
    frame.tick(frameTime)

# Start new screen section for leaderboards
screen.fill((0, 0, 0))
# Save the highest score of last playthrough
saveHighestScore(',' + str(userBlockScore) + "\n", filename="User_Scores")

# Set amount for pixel spacing in leaderboards
pixels = 40
counter = 0
# Message
displayMessage(screen, 'YOUR BEST SCORES:', LargeFont, halfWidth, 10)

# Call function to determine which global player is active
currentUser = findPlayer()
print("CURRENT PLAYER: " + currentUser + '\n')

# Open User_Scores and sort for the player's scores within all the other player's scores and return their scores
with open("User_Scores") as f:
    playerScores = [(player2, int(playerScore)) for player2, playerScore in (row.split(',') for row in f)]
    playerScores.sort(key=lambda x: x[1])
    playerScores.reverse()
    # Print out and count the scores for current player
    for element in playerScores:
        if currentUser in element:
            print("Player: " + element[0] + " Score: " + str(element[1]))
            counter += 1
            displayMessage(screen, str(counter) + ') ' + '   Score:    ' + str(element[1]), SmallerFont, halfWidth,
                           ((counter * pixels) + pixels))
    # Close file
    f.close()
pygame.display.update()

# Set events for the local scoreboard
while personal_scoreboard:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            personal_scoreboard = False
    frame.tick(frameTime)

# Start and override previous windows with Global leaderboard
screen.fill((0, 0, 0))
# Set new spacing for the window
pixels = 50
j = 0
displayMessage(screen, 'GLOBAL LEADERBOARD', LargeFont, halfWidth, 10)

# Sort the scores imported, so it can print them in order of best scores to worst
# This will encrypt the file as well
sortScores()

file = open("User_Scores", "r")
# For each line, sort through and send it to pygame screen
for line in file:
    # Split the file into two values
    fields = line.split(",")

    # Set user name and their scores
    userName = fields[0]
    userName = userName.upper()
    newScore = fields[1]
    newScore = int(newScore)
    j += 1
    print("Player: " + userName + " Score: " + str(newScore))
    # Displays scores to the leaderboard in pygame
    displayMessage(screen, str(j) + ') Player:   ' + userName + '  Score:    ' + str(newScore), SmallerFont, halfWidth,
                   ((j * pixels) + pixels))

pygame.display.update()

# Run last global leaderboard section then Quit game
while leader_board:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leader_board = False

    frame.tick(frameTime)
encryptScores()

# End
