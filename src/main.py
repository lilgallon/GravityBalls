import time
import pygame as pygame
from Ball import Ball
from utils.Vec2D import Vec2d as Vector2


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
    balls.append(Ball(300, 150, 20, (0,0,255), velocity=10, angle=140))

    clicked_ball = None
    last_tick_pos = None

    run = True
    while run:

        for event in pygame.event.get():
            current_mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT: 
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                index = 0
                while clicked_ball is None and index < len(balls):
                    if balls[index].hover(current_mouse_pos):
                        clicked_ball = balls[index]
                        clicked_ball.clicked(True)
                    else:
                        index += 1
            if event.type == pygame.MOUSEBUTTONUP:
                if clicked_ball is not None:
                    clicked_ball.clicked(False)
                    vx = current_mouse_pos[0] - last_tick_pos[0]
                    vy = current_mouse_pos[1] - last_tick_pos[1]
                    clicked_ball.set_velocity(Vector2(vx, vy))
                    clicked_ball = None

            if event.type == pygame.MOUSEMOTION:
                if clicked_ball is not None:
                    clicked_ball.set_position(current_mouse_pos)

            last_tick_pos = current_mouse_pos

        screen.fill((255,255,255))

        for i in range(0, len(balls)):
            for j in range(i + 1, len(balls)):
                 if balls[i].collides(balls[j]):
                    balls[i].handle_balls_collision(balls[j])
            balls[i].update(*screen.get_size())
            balls[i].draw(screen)
            balls[i].draw_vec(screen, size=3)
            balls[i].draw_tracker(screen)

        pygame.display.flip()
        time.sleep(0.05)


if __name__ == '__main__':
    main()