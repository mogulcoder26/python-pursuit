from turtle import Turtle
ALIGNMENT = 'center'
FONT  ='Courier'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0,y=240)
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=(FONT,24,'normal'))
        self.hideturtle()

    def increaseScore(self):
        self.score +=1
        self.clear()
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=(FONT,24,'normal'))

    def gameOver(self):
        self.clear()
        self.write(f"Game Over!Score:{self.score}",align=ALIGNMENT,font=(FONT,24,'normal'))
