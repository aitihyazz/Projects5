import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('My first py game')
img = pygame.transform.scale(pygame.image.load('ABC').convert(), (300, 300))
c=img.get_rect(center=(250,250))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((58, 58, 58))
    screen.blit(img,c )
    pygame.display.flip()
pygame.quit()
