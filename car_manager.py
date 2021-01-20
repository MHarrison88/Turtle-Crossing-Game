from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.car = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def move_fd(self):
        for each in self.car:
            each.fd(self.car_speed)

    def spawn(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1.0, stretch_len=2.0)
        new_car.pu()
        new_car.seth(180)
        new_car.goto(320, random.randint(-240, 241))
        new_car.color(random.choice(COLORS))
        self.car.append(new_car)

    def car_speedup(self):
        self.car_speed += MOVE_INCREMENT