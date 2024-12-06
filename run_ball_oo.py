import turtle
import ball_oo
import random

class BallSim:
    def __init__(self,num_balls):
        self.num_balls = num_balls
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        turtle.colormode(255)
        self.ball_list = []

        ball_radius = 0.05 * self.canvas_width
        for i in range(self.num_balls):
            x = random.uniform(-1 * self.canvas_width + ball_radius, self.canvas_width - ball_radius)
            y = random.uniform(-1 * self.canvas_height + ball_radius, self.canvas_height - ball_radius)
            vx = 10 * random.uniform(-1.0, 1.0)
            vy = 10 * random.uniform(-1.0, 1.0)
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(ball_oo.Ball(ball_color, ball_radius, x, y, vx, vy, i))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def run(self):
        dt = 0.2
        while True:
            turtle.clear()
            self.draw_border()
            for i in range(len(self.ball_list)):
                self.ball_list[i].draw()
                self.ball_list[i].move(dt)
                self.ball_list[i].update(self.canvas_height, self.canvas_width)
            turtle.update()