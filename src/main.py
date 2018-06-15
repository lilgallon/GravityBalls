import time
import pygame as pygame
from Ball import Ball


def main():
    pygame.init()

    WIDTH, HEIGHT = 700, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Gravity!')

    balls = []
    #                 x  y  vel, ang, radius, color
    balls.append(Ball(50, 50, 20, (255,0,0)))
    balls.append(Ball(100, 50, 25, (0,255,0)))
    #balls.append(Ball(50, 100, 50, 20, 40, (255,0,0)))

    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False

        screen.fill((255,255,255))

        # for i in range(0, len(balls)):
        #     for j in range(i + 1, len(balls)):
        #         if balls[i].collides(balls[j]):
        #             balls[i].handle_collision(balls[j])

        for ball in balls:
            ball.update(*screen.get_size())
            ball.draw(screen)

        # pygame.display.flip()
        pygame.display.update()
        time.sleep(0.1)


if __name__ == '__main__':
    main()