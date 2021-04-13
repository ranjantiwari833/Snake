from turtle import Screen,Turtle
from obstacle import Obstacle
import time
from snake import Snake
from food import Food
from constants import *
from scoreboard import Score

def main():
    screen = Screen()
    screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
    screen.tracer(0) #this will stop screen animation until updated
    screen.bgcolor("black")
    screen.title("My Snake Game")

    snake = Snake()
    score = Score()
    food = Food()

    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(SPEED)
        
        snake.move()
        
        #obstacles
        if score.score == 5:
            barrier = Obstacle()
        
        elif score.score ==10:
            barrier.second_obstacle()
        
        elif score.score == 15:
            barrier.third_obstacle()
        
        elif score.score == 20:
            barrier.fourth_obstacle()
        
        elif score.score == 25:
            barrier.fifth_obstacle()
            
        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            score.score_update()
            snake.extend()
        
        #detect collision with wall
        if snake.head.xcor() >X_BOUNDARY or snake.head.ycor() >Y_BOUNDARY or snake.head.xcor() < -X_BOUNDARY or snake.head.ycor() < -Y_BOUNDARY:
            game_is_on = False
            score.game_over()   
        
        #detect collision with tail
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()
        
        if score.score >5:
            for segment in barrier.body:
                if snake.head.distance(segment) < 10:
                    game_is_on = False
                    score.game_over()
        
        
    screen.exitonclick()

if __name__ == "__main__":
    main()