import pygame
from pygame.math import Vector2
import math

class Ball:
    # Density of a ball ()
    DENSITY = 0.001
    GRAVITY = 9.81
    # Impact velocity reducer (%)
    IMPACT_REDUCER = 0.20

    def __init__(self, x, y, radius, color, velocity=0, angle=0):
        """
        Arguments:
            x {int} -- x initial position
            y {int} -- y initial position
            radius {int} -- radius of the ball
            color {tuple3} -- color of the ball

        Keyword Arguments:
            velocity {int} -- initial velocity (default: {0})
            angle {int} -- initial angle (degrees) (default: {0})
        """
        # Convert the initial angle & velocity to a velocity vector
        self.velocity = Vector2(- math.cos(self.deg_to_grad(angle)) * velocity,
                               - math.sin(self.deg_to_grad(angle)) * velocity)
        self.position = Vector2(x, y)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        """ It draws the ball on the pygame screen.
        """
        pygame.draw.circle(screen,
                           self.color,
                           (int(self.position[0]), int(self.position[1])),
                           self.radius)

    def update(self, screen_width, screen_height):
        """ It updates the ball position.
        """
        print(self.position)
        # Get the screen dimensions
        width, height = screen_width, screen_height

        # Apply gravity
        self.velocity += self.get_gravity_vector()

        # Move the ball
        self.position += self.velocity

        # It has hit the right border
        if self.position[0] + self.radius > width:
            self.velocity[0] *= -1
            self.position[0] = width - self.radius
            self.velocity -= self.velocity * self.IMPACT_REDUCER
        # It has hit the left border
        elif self.position[0] - self.radius < 0:
            self.velocity[0] *= -1
            self.position[0] = self.radius
            self.velocity -= self.velocity * self.IMPACT_REDUCER
        # It has hit the top border
        if self.position[1] + self.radius > height:
            self.velocity[1] *= -1
            self.position[1] = height - self.radius
            self.velocity -= self.velocity * self.IMPACT_REDUCER
        # It has hit the bottom border
        elif self.position[1] - self.radius < 0:
            self.velocity[1] *= -1
            self.position[1] = self.radius
            self.velocity -= self.velocity * self.IMPACT_REDUCER

    def get_gravity_vector(self):
        """ It returns the gravity vector of a ball according to its mass.
        """
        area = math.pi * self.radius * self.radius
        mass = area * self.DENSITY

        return Vector2(0, mass * self.GRAVITY)

    def deg_to_grad(self, deg):
        """ Convert degrees to radian.
        """
        return deg * math.pi / 180

    # def collides(self, ball):
    #     return (math.sqrt((self.x - ball.x)**2 + (self.position[1] - ball.y)**2) <=
    #             self.radius + ball.radius)

# some help : https://stackoverflow.com/questions/345838/ball-to-ball-collision-detection-and-handling
