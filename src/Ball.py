import pygame
import math
from utils.Vec2D import Vec2d as Vector2

class Ball:
    # Density of a ball ()
    DENSITY = 0.001
    GRAVITY = 1.81
    # Impact velocity reducer (%)
    IMPACT_REDUCER = 0.15

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
        self.is_clicked = False

    def draw(self, screen):
        """ It draws the ball on the pygame screen.
        """
        pygame.draw.circle(screen,
                           self.color,
                           (int(self.position[0]), int(self.position[1])),
                           self.radius)

    def draw_vec(self, screen, size=1):
        """ It draws the velocity vector.
        """
        start = (int(self.position[0]), int(self.position[1]))
        end = (int(self.position[0] + self.velocity[0] * size),
               int(self.position[1] + self.velocity[1] * size))
        pygame.draw.line(screen, (0, 0, 0), start, end)

    def update(self, screen_width, screen_height):
        """ It updates the ball position.
        """
        # Get the screen dimensions
        width, height = screen_width, screen_height
        # Apply gravity
        if not self.is_clicked:
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

    def handle_balls_collision(self, ball):
        # Two-dimensional collision with two moving objects
        # https://en.wikipedia.org/wiki/Elastic_collision
        collision = self.position - ball.get_position()
        distance = collision.get_length()

        collision = collision / distance
        aci = self.velocity.dot(collision)
        bci = ball.get_velocity().dot(collision)
        acf = bci
        bcf = aci

        self.velocity += (acf - aci) * collision
        ball.set_velocity(ball.get_velocity() + (bcf - bci) * collision)

    def get_mass(self):
        """ It returns the mass of the ball.
        """
        area = math.pi * self.radius * self.radius
        return area * self.DENSITY

    def get_velocity(self):
        return self.velocity

    def get_position(self):
        return self.position
    
    def set_position(self, pos):
        self.position = Vector2(pos[0], pos[1])

    def set_velocity(self, velocity):
        self.velocity = velocity

    def get_gravity_vector(self):
        """ It returns the gravity vector of a ball according to its mass.
        """
        return Vector2(0, self.get_mass() * self.GRAVITY)

    def deg_to_grad(self, deg):
        """ Convert degrees to radian.
        """
        return deg * math.pi / 180

    def get_radius(self):
        return self.radius

    def collides(self, ball):
        """ Returns true if the current ball collides the <ball>
        """
        distance = self.position.get_distance(ball.get_position())
        return distance <= self.radius + ball.get_radius()

    def hover(self, pos):
        return (pos[0] < self.position[0] + self.radius and
                pos[0] > self.position[0] - self.radius and
                pos[1] < self.position[1] + self.radius and
                pos[1] > self.position[1] - self.radius)

    def clicked(self, is_clicked):
        self.is_clicked = is_clicked
        if is_clicked:
            self.velocity = Vector2(0, 0)


# some help : https://en.wikipedia.org/wiki/Elastic_collision
