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
        try:
            f = open("highscore.txt","r")
            self.highscore = int(f.read())
            f.close()
        except:
            f = open("highscore.txt","w")
            self.highscore = 0
            f.write('0')
            f.close()
        self.write(f"Score : {self.score},High Score : {self.highscore}",align=ALIGNMENT,font=(FONT,24,'normal'))
        self.hideturtle()

    def increaseScore(self):
        self.score +=1
        f = open('highscore.txt','r')
        highscore = int(f.read())
        if(highscore <= self.score):
            x = open('highscore.txt','w')
            x.write(f"{self.score}")
            self.highscore = self.score
            x.close()
        f.close()
        self.clear()
        self.write(f"Score : {self.score},High Score : {self.highscore}",align=ALIGNMENT,font=(FONT,24,'normal'))

    def gameOver(self):
        self.clear()
        self.write(f"Game Over!Score:{self.score}",align=ALIGNMENT,font=(FONT,24,'normal'))
