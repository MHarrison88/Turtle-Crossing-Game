import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Cross")
screen.tracer(0)

p1 = Player()
cars = CarManager()
score = Scoreboard()

loop = 0

screen.listen()
screen.onkeypress(fun=p1.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    loop += 1
    if loop % 6 == 0:
        cars.spawn()

    cars.move_fd()

    for each in cars.car:
        if p1.distance(each) < 20:
            game_is_on = False
            score.game_over()
    
    if p1.finish():
        p1.restart()
        cars.car_speedup()
        score.score()
    
screen.exitonclick()