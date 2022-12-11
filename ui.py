from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)
        self.main_text = self.canvas.create_text(150, 125, text="Some Question text",
                                                 fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, font=("Arial", 15,))
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()