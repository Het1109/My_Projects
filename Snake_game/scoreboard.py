from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier" ,24 ,"normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open("highscore.txt" ) as data :
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0 , 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}" , align= ALIGNMENT , font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt" , mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()


    #
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over!" , align= ALIGNMENT , font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()
