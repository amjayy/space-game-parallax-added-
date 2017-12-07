import pygame
from settings import Settings
from alienlady import Alienlady


pygame.init()
pygame.mixer.init()
ai_settings=Settings()
screen =  pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption( "Space Queen Showdown")
pygame.mixer.music.load("music/Aaliyah.mp3")
pygame.mixer.music.play(0)

alienlady= Alienlady(screen)

done = False
clock = pygame.time.Clock()
background_position = [0, 0]
alienlady_positon=[450, 300]
background_image = pygame.image.load("images/spacebridge.jpg")

player = pygame.image.load("images/alienlady.png")


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            alienlady.blitme()
            
    screen.blit(background_image, background_position)

    pygame.display.flip()

    clock.tick(60)

    
