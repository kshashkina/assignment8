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


WIDTH = 600
HEIGHT = 600
lives = 3
paddle = Paddle(250, 550, 100, 25)
ball = Ball(300, 500, 10, 3, -3)


def draw():
    screen.fill((99, 112, 105))
    paddle.draw()
    ball.draw()


def update():
    global lives
    paddle.on_mouse_move(pygame.mouse.get_pos())
    ball.update()
    # check if the ball hits the paddle
    if ball.y + ball.radius >= paddle.y - paddle.height and pygame.mouse.get_pos()[0] <= ball.x <= \
            pygame.mouse.get_pos()[0] + paddle.width:
        ball.speed_y *= -1
        # if paddle is really close to the walls, ball changes its direction along x-axis (more variety in ball movements)
        if pygame.mouse.get_pos()[0] + paddle.width <= 125 or pygame.mouse.get_pos()[0] + paddle.width >= 575:
            ball.speed_x *= -1
    # check if ball is under the paddle
    if ball.y + ball.radius >= HEIGHT:
        lives -= 1
        ball.x = pygame.mouse.get_pos()[0]
        ball.y = 500
        ball.speed_x = 3
        ball.speed_y = -3


pgzrun.go()
