import time
import pygame as pygame
from Ball import Ball


def main():
    pygame.init()

    WIDTH, HEIGHT = 700, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Gravity!')

    balls = []
    balls.append(Ball(50, 50, 20, (255,0,0), velocity=20))
    balls.append(Ball(100, 50, 25, (0,255,0)))
    balls.append(Ball(50, 100, 20, (255,0,0), velocity=20))
    balls.append(Ball(150, 150, 20, (255,0,0), velocity=30))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False

        screen.fill((255,255,255))

        for i in range(0, len(balls)):
            balls[i].handle_border_collision(*screen.get_size())
            for j in range(i + 1, len(balls)):
                 if balls[i].collides(balls[j]):
                     balls[i].handle_balls_collision(balls[j])
            balls[i].draw(screen)
            balls[i].draw_vec(screen, size=3)

        # pygame.display.flip()
        pygame.display.update()
        time.sleep(0.05)


if __name__ == '__main__':
    main()