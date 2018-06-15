import time
import pygame as pygame
from Ball import Ball


def main():
    pygame.init()

    WIDTH, HEIGHT = 500, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Gravity!')

    balls = []
    #                 x  y  vel, ang, radius, color
    balls.append(Ball(50, 50, 20, 20, 40, (255,0,0)))
    balls.append(Ball(100, 150, 20, 250, 40, (0,255,0)))
    #balls.append(Ball(50, 100, 50, 20, 40, (255,0,0)))

    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False

        screen.fill((255,255,255))
        # Pareil ?
        for ball in balls:
            ball.update(screen, balls)

        # pygame.display.flip()
        pygame.display.update()
        time.sleep(0.1)

if __name__ == '__main__':
    main()