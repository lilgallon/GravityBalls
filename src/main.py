import time
import pygame as pygame
from Ball import Ball


def main():
    pygame.init()

    WIDTH, HEIGHT = 300, 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Gravity!')

    ball = Ball(100, 50, 10, 200, 20, (255,0,0))

    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False

        screen.fill((255,255,255))
        # Pareil ?
        ball.update(screen)
        # pygame.display.flip()
        pygame.display.update()

        time.sleep(0.1)

if __name__ == '__main__':
    main()