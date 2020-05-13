def findWaitingTime(n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def findTurnAroundTime(n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(bt):
    n=len(bt)
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime( n, bt, wt)
    findTurnAroundTime( n, bt, wt, tat)
    print("Processes" + "  Burst time " + " Waiting time " + " Turn around time")

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t\t\t" + str(bt[i]) + "\t\t\t " +str(wt[i]) + "\t\t\t\t " + str(tat[i]))

    print("Average waiting time = " + str(total_wt / n))
    print("Average turn around time = " + str(total_tat / n))
    return bt,wt,tat
