import tkinter as tk
import Abc
import random

r = tk.Tk()
r.title("SIMULATION")
r.geometry("430x200")
r.configure(background="black")
n=[]
for i in range(5):
    n.append(random.choice([1,2,3,4,5]))
def fcfs():
    r.destroy()
    Abc.run(n,1)

def roundrobin():
    r.destroy()
    Abc.run(n,2)

l = tk.Label(r, text="CPU SCHEDULING ALGORITHM", fg="pale green", background="black", font=("Helvetica", 16))
l.place(x=80, y=20)
b1 = tk.Button(r, text="FCFS", command=fcfs, activeforeground="black", activebackground="gray19", width=7,
               bg="thistle4")
b1.place(x=130, y=140)

b2 = tk.Button(r, text="RR", command=roundrobin, activeforeground="black", activebackground="gray19", width=7,
               bg="thistle4")
b2.place(x=240, y=140)

r.mainloop()