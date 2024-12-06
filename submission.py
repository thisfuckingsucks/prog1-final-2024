from seven_segement_oo import Display
from run_ball_oo import BallSim
import turtle

class DuelSim(BallSim, Display):
    def __init__(self,num_balls,my_turtle,color):
        BallSim.__init__(self,num_balls)
        Display.__init__(self,my_turtle,color)

    def run(self):
        print('DuelSim')
        dt = 0.2
        i = 0
        while True:
            self.clear()
            self.drawN(i)
            self.my_delay(dt)
            turtle.clear()
            self.draw_border()
            for k in range(len(self.ball_list)):
                self.ball_list[k].draw()
                self.ball_list[k].move(dt)
                self.ball_list[k].update(self.canvas_height, self.canvas_width)
            turtle.update()
            i = i+1
            if i >= 10:
                i = 0
            print(i)

Tom = turtle.Turtle()
tom_color = (255, 0, 0)
shio = DuelSim(5, Tom, tom_color)
shio.run()