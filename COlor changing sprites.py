import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 400))

def randomc():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
)

changecolor = pygame.USEREVENT + 1

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, hight, width):
        super().__init__()
        self.image = pygame.Surface([width, hight])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def cchangef(self, newcolor):
        self.image.fill(newcolor)

sprite1 = Sprite((225, 0, 0), 50, 50)
sprite2 = Sprite((125, 0, 0), 50, 50)

# Fix rect position
sprite1.rect.center = (100, 150)
sprite2.rect.center = (300, 150)

all = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False

        if event.type == changecolor:
            sprite1.cchangef(randomc())  
            sprite2.cchangef(randomc())  

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        pygame.event.post(pygame.event.Event(changecolor))

    all.update()
    screen.fill((0, 0, 0))
    all.draw(screen)
    pygame.display.flip()

pygame.quit()
