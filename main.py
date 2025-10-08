from tkinter import *
import tkinter.font as font 

my_window = Tk()
my_window.geometry("300x300")

description = Label(my_window, text="Temperature in Farenheit", font=font.Font(size=20),fg = "grey")
description.pack()

frame = Frame(my_window)
frame.pack(pady=20)

message_one = Label(frame, text="Enter Temperature in Celsius :", font=font.Font(size=15))
message_one.grid(row=0, column=0)

celsius_value = Entry(frame)
celsius_value.grid(row=0, column=1)

error_msg = Label(frame,text="Please enter valid input", font=font.Font(size=8), fg="red")

output_farenheit = Label(frame, font=font.Font(size=12))
output_farenheit.grid(row=2, column = 0, columnspan=2, pady=10)

submit_btn = Button(frame, text="Convert", width = 30, fg = "Black", bg = "light green", bd = 0, padx = 20, pady = 10= command = convert)
submit_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10)

my_window.geomitry("500x250")
my_window.mainloop()