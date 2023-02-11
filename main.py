#Digital Clock

from tkinter import Tk
from tkinter import Label
import time
root = Tk()
root.title("Clock")
def present_time():
    disp_time = time.strftime("%I:%M:%S %p")
    digi_clk.config(text=disp_time)
    digi_clk.after(1000,present_time)

digi_clk = Label(root, font=("arial",150),bg="black",fg="green")
present_time()
digi_clk.pack()
root.mainloop()



