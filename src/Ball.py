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

        self.vx = math.cos(self.deg_to_grad(angle)) * velocity
        self.vy = math.sin(self.deg_to_grad(angle)) * velocity
        self.x = x
        self.y = y
        self.angle = angle
        self.radius = radius
        self.color = color
        self.gravity = 9
        self.friction = 0.5

    def update(self, screen):
        width, height = screen.get_size()

        self.vy += self.gravity

        self.x += self.vx
        self.y += self.vy

        if self.x + self.radius > width:
            self.vx *= -1
            self.x = width - self.radius
        elif self.x - self.radius < 0:
            self.vx *= -1
            self.x = self.radius

        if self.y + self.radius > height:
            self.vy *= -1
            self.y = height - self.radius
        elif self.y - self.radius < 0:
            self.vy *= -1
            self.y = self.radius

        if self.y + self.radius == height:
            if self.vx > 0:
                if self.vx - self.friction < 0:
                    self.vx = 0
                else:
                    self.vx -= self.friction
            elif self.vx < 0:
                if self.vx + self.friction > 0:
                    self.vx = 0
                else:
                    self.vx += self.friction

        self.x = int(self.x)
        self.y = int(self.y)

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def deg_to_grad(self, deg):
        return deg * math.pi / 180


