import pygame

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((200,200))

eye1 = pygame.Rect(50,50,30,15)
eye2 = pygame.Rect(120,50,30,15)
lips1 = pygame.Rect(25,125,30,10)
lips2 = pygame.Rect(55,125,30,10)
lips3 = pygame.Rect(85,125,30,10)
lips4 = pygame.Rect(115,125,30,10)
lips5 = pygame.Rect(145,125,30,10)

while True:    
    screen.fill((150,75,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
                 
    pygame.draw.rect(screen,(0,0,0), eye1)
    pygame.draw.rect(screen,(0,0,0), eye2)
    pygame.draw.rect(screen,(0,0,0), lips1)
    pygame.draw.rect(screen,(0,0,0), lips2)
    pygame.draw.rect(screen,(0,0,0), lips3)
    pygame.draw.rect(screen,(0,0,0), lips4)
    pygame.draw.rect(screen,(0,0,0), lips5)
  
    pygame.display.update()