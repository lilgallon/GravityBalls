import pygame
import math

class Ball:
    def __init__(self, x, y, velocity, angle, radius, color):
        """[summary]
        
        Arguments:
            x {[type]} -- [description]
            y {[type]} -- [description]
            velocity {[type]} -- pixel / tick
            radius {[type]} -- [description]
            color {[type]} -- [description]
        """
        # - because axis are inverted
        self.vx = - math.cos(self.deg_to_grad(angle)) * velocity
        self.vy = - math.sin(self.deg_to_grad(angle)) * velocity
        self.x = x
        self.y = y
        self.angle = angle
        self.radius = radius
        self.color = color
        self.gravity = 9
        self.impact_reducer = 20  # %

    def update(self, screen, balls):
        width, height = screen.get_size()

        self.vy += self.gravity

        self.x += self.vx
        self.y += self.vy

        for ball in balls:
            if self.collide(ball):
                if self == ball:
                    continue
                print('x: ' + str(self.x) + ' ' + str(ball.get_pos()[0]))
                print('y: ' + str(self.y) + ' ' + str(ball.get_pos()[1]))
                # line that pass through the two balls
                a = (ball.y - self.y) / (ball.x - self.x)
                b = self.y - a * self.x
                # distance between the two balls
                # dist = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
                self.x += a
                self.y += b
                print('a ' + str(a))
                print(b)
                if b >= 0:
                    self.vx *= -1
                    self.friction(self.impact_reducer)
                elif b < 0:
                    self.vy *= -1
                    self.friction(self.impact_reducer)

        if self.x + self.radius > width:
            self.vx *= -1
            self.x = width - self.radius
            self.friction(self.impact_reducer)
        elif self.x - self.radius < 0:
            self.vx *= -1
            self.x = self.radius
            self.friction(self.impact_reducer)

        if self.y + self.radius > height:
            self.vy *= -1
            self.y = height - self.radius
            self.friction(self.impact_reducer)
        elif self.y - self.radius < 0:
            self.vy *= -1
            self.y = self.radius
            self.friction(self.impact_reducer)

        self.x = int(self.x)
        self.y = int(self.y)

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def deg_to_grad(self, deg):
        return deg * math.pi / 180

    def friction(self, percentage):
        self.vx -= self.vx * percentage / 100
        self.vy -= self.vy * percentage / 100

    def get_vecs(self):
        return (self.vx, self.vy)

    def get_pos(self):
        return (self.x, self.y)

    def collide(self, ball):
        return (math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2) <=
                self.radius + ball.radius)

# some help : https://stackoverflow.com/questions/345838/ball-to-ball-collision-detection-and-handling
