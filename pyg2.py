import pygame
pygame.init()
a = pygame.display.set_mode((600,600))
rect = pygame.Rect(10, 20, 60, 60) 
rect.center = (300, 300)  
font=pygame.font.SysFont('Arial',32)

text = font.render("Hello, Pygame!", True, (255, 25, 250))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    a.fill((255, 255, 255)) 
    pygame.draw.rect(a, (0, 0, 0), rect, 0)  
    a.blit(text, (100, 100))
    pygame.display.flip()  