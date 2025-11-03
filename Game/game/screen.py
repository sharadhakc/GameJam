import pygame

pygame.init()
screenWidth=1200
screenHeight=800

font = pygame.font.Font(None, 50)


text_color = (255, 255, 255) # White


button = pygame.transform.scale(pygame.image.load("Assets/start.png"), (200, 75))

background = pygame.transform.scale(pygame.image.load("Assets/title.jpg"), (screenWidth, screenHeight))

button_rect = pygame.Rect(screenWidth//2 - 100, screenHeight//2, 200, 75)

title_screen = {
    "background": background,
    "text": font.render("Alien Blaster", True, text_color),
    "start": button,
    "button_rect": button_rect,
    "score": font.render("Highest score:", True, text_color),
}

