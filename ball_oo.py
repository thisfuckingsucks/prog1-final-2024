import turtle

class Ball:
    def __init__(self,color,size,x,y,vx,vy,i):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.i = i

    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self,dt):
        self.x += self.vx*dt
        self.y += self.vy*dt

    def update(self,canvas_height,canvas_width):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x) > (canvas_width - self.size):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y) > (canvas_height - self.size):
            self.vy = -self.vy