import pygame

pygame.init()
screenWidth=1200
screenHeight=800

font = pygame.font.Font(None, 36)


text_color = (255, 255, 255) # White


button = pygame.transform.scale(pygame.image.load("Assets/start.png"), (100, 100))

background = pygame.transform.scale(pygame.image.load("Assets/title.jpg"), (screenWidth, screenHeight))

title_screen = {
    "background": background,
    "text": font.render("Shooter", True, text_color),
    "start": button

}

end_screen = {
    "background": background,
    "text": font.render("Game Over", True, text_color),
    "start": button

}