import tkinter as Tk

window = Tk.Tk()



window.title("H@ck Attack")
window.geometry('800x600')
window.configure(background = '#007dba')

val = ''
val = 'a'

score = 0

label = Tk.Label(window, text = "Cyber Defence - H@ck Attack Game")

question = Tk.Label(window, text = 'This is where the question will be', pady = 10)

button_a = Tk.Radiobutton(window, bg = 'white', text = 'Temp A', variable = val, value = 'a', indicatoron = 0, width = 300, padx = 20)
button_b = Tk.Radiobutton(window, bg = 'white', text = 'Temp B', variable = val, value = 'b', indicatoron = 0, width = 300, padx = 20)
button_c = Tk.Radiobutton(window, bg = 'white', text = 'Temp C', variable = val, value = 'c', indicatoron = 0, width = 300, padx = 20)
button_d = Tk.Radiobutton(window, bg = 'white', text = 'Temp D', variable = val, value = 'd', indicatoron = 0, width = 300, padx = 20)

img = Tk.PhotoImage(file='TempImg2.gif')
image_display = Tk.Label(window, image = img)

score_label = Tk.Label(window, text = 'Score = ')
current_score = Tk. Label(window, text = score)

label.pack(side='top')
image_display.pack(side='top')
question.pack(side='top')
button_a.pack(side='top')
button_b.pack(side='top')
button_c.pack(side='top')
button_d.pack(side='top')
score_label.pack(side='left')
current_score.pack(side='right')

window.mainloop()