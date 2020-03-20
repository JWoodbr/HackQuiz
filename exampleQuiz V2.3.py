from tkinter import *
import random
     
class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            answer_label = Label(x, text="That's right!", bg='green')
            right += 1
        else:
            answer_label = Label(x, text="Oooh, That's not quite right...", bg='red')
        view.pack_forget()   
        answer_label.pack()
        x.after(1000, lambda *args: answer_label.destroy())
        view.after(1000, lambda *args: self.unpackView(view))
        
        

    def getView(self, window):
        view = Frame(window)

        Label(view, text=self.question, wraplength=500).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + "\n questions answered right", wraplength=500).pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

def choosequestions():
    questionsfile = ""
    randq = random.randint(1,3)
    if (randq == 1):
        questionsfile = "questions1.txt"
    elif (randq == 2):
        questionsfile = "questions2.txt"
    else:
        questionsfile = "questions3.txt"
    return questionsfile
 
questions = []
qfile = choosequestions()
file = open(qfile, "r")
line = file.readline()
while(line != "[end]"):
    if line == "[end]":
        break
    questionString = line
    answers = []
    for i in range(4):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)



window = Tk()
window.title("H@ck Attack")
window.geometry('800x600')
window.configure(background = '#007dba')

img = PhotoImage(file='anz.gif')
image_display = Label(window, image = img)

image_display.pack(side='top')

x = Frame(window)
x.pack(side='top')

button = Button(window, text="Start", command=askQuestion)
button.pack()

window.mainloop()