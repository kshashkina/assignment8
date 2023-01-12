import pgzrun
import pygame
import random


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
# create two lists with random x-axis position of falling objects
heart_fall_x = [random.randint(50, 550) for i in range(4)]
arrow_fall_x = [random.randint(50, 550) for o in range(4)]
ind_heart = 0
ind_arrow = 0
heart = Actor("heart", (heart_fall_x[ind_heart], -60 * 30))
arrow = Actor("arrow", (arrow_fall_x[ind_arrow], -60 * 15))


def draw():
    screen.fill((99, 112, 105))
    paddle.draw()
    ball.draw()
    heart.draw()
    arrow.draw()
    if lives == 0:
        screen.draw.text("GAME   OVER!", (150, 300), fontname="font", fontsize=60)


def update():
    global lives, paddle, heart, arrow, ind_heart, ind_arrow
    paddle.on_mouse_move(pygame.mouse.get_pos())
    ball.update()
    heart.bottom += 1
    arrow.bottom += 1
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
        # if game is over -> stop movement of ball
        if lives == 0:
            ball.speed_x = 0
            ball.speed_y = 0
    # check if heart is bellow the screen, it was not collided with paddle and return it to its position at the top
    if heart.bottom >= HEIGHT and ind_heart != 3:
        heart.pos = (heart_fall_x[ind_heart], -60 * 30)
    # check heart and paddle collision and return it to the top with another x-position
    if heart.colliderect(paddle.rect):
        ind_heart += 1
        heart.pos = (heart_fall_x[ind_heart], -60 * 30)
        lives += 1
        # max amount of hearts that can be taken during game is 3, check if this amount is greater than 3
        # and remove heart from screen
        if ind_heart == 3:
            heart.pos = (-100, -100)
    # check if arrow is bellow screen and was not collided with paddle and return it to its position at top
    if arrow.bottom >= HEIGHT and ind_arrow != 3:
        arrow.pos = (arrow_fall_x[ind_heart], -60 * 15)
    # check arrow and paddle collision and return it to the top with another x-position + make paddle bigger
    if arrow.colliderect(paddle.rect):
        ind_arrow += 1
        paddle = Paddle(250, 550, 200, 25)
        arrow.pos = (arrow_fall_x[ind_arrow], -60 * 8 - (60 * 15))
        # max amount of arrow that can be taken during game is 3, check if this amount is greater than 3
        # and remove arrow from screen
        if ind_arrow == 3:
            arrow.pos = (-100, -100)
    # after certain amount of time change size of paddle to the previous size:
    if arrow.pos == (arrow_fall_x[ind_arrow], -800) or arrow.pos == (-100, 700):
        paddle = Paddle(250, 550, 100, 25)



pgzrun.go()
