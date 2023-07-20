from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
starting_coords = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Python Pursuit')
screen.tracer(0)
segment_array = []

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down') 
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_over = False

while(not(game_over)):
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Why Error ?
    #Detection of Collision
    # print([snake.head.xcor(),food.xcor()],[snake.head.ycor(),food.ycor])
    # print()
    # if(snake.head.xcor()==food.xcor() and snake.head.ycor() == food.ycor()):
    #     # print('Collision')
    #     exit()

    if(snake.head.distance(food)<20):
        print('Nom Nom Nom') 
        snake.SnakeAteFoodSoSnakeExtends() 
        food.refresh()
        score.increaseScore()
    
    #Detect Collision with Wall:

    if(snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
        game_over = True
        score.gameOver()

    #Detect Collision with Snake itself:
    for segment in snake.segment_array[1:len(snake.segment_array)+1]:
        # if segment is snake.head:
        #     continue
         if(snake.head.distance(segment)<15):
            game_over=True
            score.gameOver()
    

screen.exitonclick()
