from graphics import *
import Main

c = []

colours = ['red', 'green', 'blue', 'yellow', 'white', 'orange', 'purple', 'pink', 'grey', 'light blue']


def main(n):
    global win
    win = GraphWin('Simulation', 700, 500)
    win.setBackground('black')
    for i in range(len(n)):
        for j in range(n[i]):
            d = Circle(Point((j + 1) * 20, (i + 1) * 20 + (i * 5)), 10)
            d.draw(win)
            d.setFill(colours[i])
            c.append(d)

    message = Text(Point(380, 30 * len(n) - 20), "SIMULATION")
    message.setTextColor('white')
    message.draw(win)
    time.sleep(1)


def fcfs(n):
    message = Text(Point(380, 20), "FIRST COME FIRST SERVE")
    message.setTextColor('white')
    message.draw(win)
    time.sleep(1)
    '''for i in range(sum(n)):
        c[i].move(i,20*(len(n)+1)+(len(n)*5))
        time.sleep(1)'''
    index = 0
    x = 0
    for i in range(len(n)):
        for j in range(n[i]):
            c[index].move(sum(n[0:i]) * 20, 30 * (len(n) + 1) - (i * 25))
            index += 1
            x += 1
            time.sleep(1)


def rr(n):
    message = Text(Point(380, 20), "ROUND ROBIN")
    message.setTextColor('white')
    message.draw(win)
    time.sleep(1)
    a = [0]
    s = [n[0]]
    for i in range(1, len(n)):
        a.append(sum(n[0:i]))
        s.append(sum(n[0:i + 1]))

    t = 0
    for i in range(max(n)):
        for j in range(len(n)):
            if a[j] + i < s[j]:
                c[a[j] + i].move(t, 30 * len(n) - (25 * j))
                t += 20
                time.sleep(1)
        t -= 20

    win.close()


def run(n,x):
    main(n)
    if x == 1:
        fcfs(n)
        bt, wt, tat = Main.fstat(n)
    else:
        rr(n)
        bt, wt, tat = Main.rstat(n)
    r = tk.Tk()
    r.title("Statistics")
    r.geometry("600x350")
    r.configure(background="black")
    l1 = tk.Label(r, text="Total burst time: " + str(sum(bt)), fg="white", background="black", font=("Times", 14))
    l1.place(x=50, y=200)
    l2 = tk.Label(r, text="Average waiting time: " + str(sum(wt) / len(wt)), fg="white", background="black",
                  font=("Times", 14))
    l2.place(x=50, y=230)
    l3 = tk.Label(r, text="Average turn around  time: " + str(sum(tat) / len(tat)), fg="white", background="black",
                  font=("Times", 14))
    l3.place(x=50, y=260)
    tk.Label(r, text="Processes" + "  Burst time " + " Waiting time " + " Turn around time", fg="white", background="black", font=("Times", 14)).grid(row=0, column=0,padx=5)
    for r1 in range(len(n)):
        tk.Label(r, text='%s\t%s\t%s\t%s' % (r1 + 1, bt[r1], wt[r1], tat[r1]),borderwidth=1, fg="white", background="black", font=("Times", 14)).grid(row=r1 + 3, column=0)
    r.mainloop()




