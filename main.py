import pgzrun
import pygame


# create a Paddle Class
class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect((self.x, self.y), (self.width, self.height))

    # draw a Paddle
    def draw(self):
        screen.draw.filled_rect(self.rect, (25, 31, 28))

    # update Paddle movement according to the x-axis position of the mouse
    def on_mouse_move(self, pos: tuple):
        self.rect.left = pos[0]
        self.rect.bottom = 550


# create a ball
class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    # draw a ball
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, (255, 255, 255))

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # check if the ball hits a wall and changes its direction
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y - self.radius <= 0:
            self.speed_y *= -1


class Obstacle:
    def __init__(self, x, y, radius, collisions):
        self.x = x
        self.y = y
        self.radius = radius
        self.collisions = collisions

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, (25, 31, 28))
