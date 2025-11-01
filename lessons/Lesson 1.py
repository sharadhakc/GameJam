import pygame   # Importing Pygame library
import sys      # Importing sys library to properly close the game

# Starts up Pygame
pygame.init()

# Setting the game window's dimensions
screenWidth = 800
screenHeight = 600

# Creating a screen variable with the window dimension variables set above
# when setting window dimensions have to do .set_mode( (_,_) )

# Treat the (_,_) as order pairs inside of ( (_,_) )
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Sets the name of the window icon to "Parkour"
pygame.display.set_caption("Parkour")

# Sets the background color based of of RGB (255,255,255)
# the color is black is (0,0,0)
backgroundColor = (0,0,0)

running = True


while running:

    # Checks for user input
    for event in pygame.event.get():
       
       # Checks specifically for input on the exit button 
       # On top right of winow
       if event.type == pygame.QUIT:
          # Stops the game if the user clicks the exit button
          pygame.quit()
          sys.exit()
          running = False
    
    # Fills the window with the background color otherwise
    screen.fill(backgroundColor)

    # Updates every single window might want to 
    # change to pygame.display.update() to only update one window
    pygame.display.flip()