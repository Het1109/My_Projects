from tkinter import  *
from quiz_brain import  QuizBrain

THEME_COLOR = "#375362"

class QuizInterface :

    def __init__(self , quiz_brain : QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz_Game_API")

        self.window.config(padx= 20,
                           pady = 20 ,
                           bg= THEME_COLOR)

        self.label_score = Label(text=f"Score : {0}" , fg="white" , bg= THEME_COLOR)
        self.label_score.grid(row = 0 , column = 1)

        self.canvas = Canvas(width=300 , height=250 , bg="white" )
        self.canvas_text = self.canvas.create_text(
                     150 ,
                   125 ,
                    width= 280 ,
                   text="Some " ,
                   fill=THEME_COLOR,
                    font=("Arial" , 20 , "italic"),
                   )
        self.canvas.grid(row = 1 , column = 0 , columnspan = 2 , pady = 50)


        true_img = PhotoImage(file="images/true.png")
        self.green = Button( image= true_img , highlightthickness=0 , command= self.true_pressed)
        self.green.grid(row=2, column=1)


        false_img = PhotoImage(file="images/false.png")
        self.red = Button( image=false_img , highlightthickness=0 , command= self.false_pressed)
        self.red.grid(row=2, column=0)


        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text , text = q_text)

        else:
            self.canvas.itemconfig(self.canvas_text , text = "You have completed the quiz")
            self.green.config(state = "disabled")
            self.red.config(state = "disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")

    def give_feedback (self , is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000 ,self.get_next_question )