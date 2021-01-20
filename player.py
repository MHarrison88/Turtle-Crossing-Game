from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
cars = CarManager()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        return False
    
