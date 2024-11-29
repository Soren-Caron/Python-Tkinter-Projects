from tkinter import *
from time import *

def update():
  #directives %I, %M, %S respectively format Hour, Minute, and seconds by the tuple received from localtime()
  time_string = strftime("%I:%M:%S %p")
  clock_label.config(text=time_string)
  
  week_string = strftime("%A")
  week_label.config(text=week_string)
  
  date_string = strftime("%B %d, %Y")
  date_label.config(text=date_string)
  
  window.after(1000,update)

window = Tk()
window.title("Clock")

clock_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
clock_label.pack()

week_label = Label(window, font=("Ink Free", 25))
week_label.pack()

date_label = Label(window, font=("Ink Free", 30))
date_label.pack()

update()

window.mainloop()