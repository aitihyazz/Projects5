import pygame
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500


class Sprite(pygame.sprite.Sprite):
    def __init__(self,color, height ,width,x,y,movable=False):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(SURFACE_COLOR)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=3
        self.movable=movable
    def update(self, keys=None):
        if self.movable and keys:
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
            self.rect.x=max(0,min(self.rect.x,WIDTH-self.rect.width))
            self.rect.y=max(0,min(self.rect.y,HEIGHT-self.rect.height))
def main():
    pygame.init()
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    alls=pygame.sprite.Group()
    s1= Sprite((255, 0, 0), 50, 50, 100, 100, movable=True)
    s2=Sprite((0, 0, 255), 50, 50, 300, 300)
    alls.add(s1,s2)
    clock=pygame.time.Clock
    running =True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys=pygame.key.get_pressed()
        for sprite in alls:
            sprite.update(keys)
        screen.fill((255, 255, 255))
        alls.draw(screen)
        pygame.display.flip()
       
    
    pygame.quit()

if __name__ == "__main__":
    main()
