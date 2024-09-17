import psutil as psu
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
#importing all the modules that are required for this code

print("Your cpu has", psu.cpu_count(logical = False), "cores")
print("Your cpu has", psu.cpu_count(), "threads")
#printing the specifications for the CPU, cores and threads
cpu_speed = psu.cpu_percent(interval=2, percpu=True)
print(cpu_speed)
#printing the CPU percentage at the time when the code is intially ran

fig = plt.figure() #set the variable fig to plot.figure
fig.patch.set_facecolor('xkcd:eggshell')
ax = fig.add_subplot(111) #set the x axis variable
y = deque([-1]*150) #set the y axis, deque is a queue that data can be inserted and deleted from allowing real time updates

ax.set_xlim(0,15) #setting limiters for x and y
ax.set_ylim(0,15)

def animate_frame(i): #creating the animation fucntion
    y.pop()
    y.appendleft(int(psu.cpu_percent(None, False)))

    ax.clear() #this plots the graph 
    ax.plot(y, color = "red") #some graph customisations 
    ax.set_facecolor('xkcd:eggshell')
    ax.set_xlim([0, 100])
    ax.set_ylim([0,100])
    ax.set_xlabel("Time")
    ax.set_ylabel("CPU percentage")
    ax.set_title("CPU percentage over time")


animation = animation.FuncAnimation(fig, animate_frame, interval = 100) 
#this is the animation is runs the function with an interval of 10, this can be changed to make the graph update faster or slower
plt.show() #displays the plot/graph
