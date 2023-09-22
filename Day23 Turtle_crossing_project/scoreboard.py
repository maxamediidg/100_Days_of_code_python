from  turtle import  Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboar()

    def update_scoreboar(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)


    def increae_level(self):
        self.level +=1
        self.update_scoreboar()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME_OVER: {self.level}", align="Center", font=FONT)

