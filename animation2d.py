from platypus.algorithms import NSGAII, IBEA, CMAES, GDE3, MOEAD, OMOPSO, SMPSO, SPEA2, EpsMOEA
from platypus.problems import DTLZ2
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

problem = DTLZ2(2)

# *****SELECT THE ALGORITHM TO RUN*****
# NSGAII(problem)
# NSGAIII(problem, divisions_outer=12)
# CMAES(problem, epsilons=[0.05])
# GDE3(problem)
# IBEA(problem)
# MOEAD(problem)
# OMOPSO(problem, epsilons=[0.05])
# SMPSO(problem)
# SPEA2(problem)
# EpsMOEA(problem, epsilons=[0.05])
algorithm = NSGAII(problem)

# store algorithm state after each function evaluation
states = []
def save_state(algorithm):
    # save only every 1000th evaluation
    if algorithm.nfe % 100 == 0:
        states.append([s.objectives for s in algorithm.population])
        print(f"Saved state at evaluation {algorithm.nfe}, total states: {len(states)}")


# attach callback to the algorithm
algorithm.step_callback = save_state

# run the algorithm step by step
# run the algorithm until we reach 10,000 function evaluations
count = 0
while count < 10000:
    algorithm.step()
    save_state(algorithm)
    count += 100

# setup the plot1
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(111)

# setup the animation1
def animate1(i1):
    ax1.cla()  # clear the current plot
    objectives = states[i1]
    ax1.scatter([o[0] for o in objectives], 
               [o[1] for o in objectives])
    ax1.set_xlim([0, 1.5])
    ax1.set_ylim([0, 1.5])
    # ax1.view_init(30)
    ax1.set_title(f"{algorithm.__class__.__name__ } at evaluation {(i1+1)*1000}")

ani = FuncAnimation(fig1, animate1, frames=len(states), interval=50, repeat=False)

# save the animation as a gif file
ani.save(f'{algorithm.__class__.__name__ }-1-2d.gif', writer='pillow')

# setup the plot1
# fig2 = plt.figure(figsize=(10, 6))
# ax2 = fig2.add_subplot(111)

# # setup the animation2
# def animate2(i2):
#     ax2.cla()  # clear the current plot
#     objectives = states[i2]
#     ax2.scatter([o[0] for o in objectives], 
#                [o[1] for o in objectives])
#     ax2.set_xlim([0, 1.3])
#     ax2.set_ylim([0, 1.3])
#     ax2.set_title(f"{algorithm.__class__.__name__ } at evaluation {(i2+1)*1000}")

# ani = FuncAnimation(fig2, animate2, frames=len(states), interval=50, repeat=False)

# # save the animation as a gif file
# ani.save(f'{algorithm.__class__.__name__ }-2-2d.gif', writer='pillow')
