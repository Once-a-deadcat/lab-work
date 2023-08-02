from platypus.algorithms import *
from platypus.problems import DTLZ2
from platypus.indicators import  Hypervolume

problem = DTLZ2(3)

# setup the comparison
algorithms = [NSGAII(problem),
              NSGAIII(problem, divisions_outer=12),
              CMAES(problem, epsilons=[0.05]),
              GDE3(problem),
              IBEA(problem),
              MOEAD(problem),
              OMOPSO(problem, epsilons=[0.05]),
              SMPSO(problem),
              SPEA2(problem),
              EpsMOEA(problem, epsilons=[0.05])]

# run each algorithm for 10,000 function evaluations
for a in algorithms:
  a.run(10000)

# compute and print the hypervolume
hyp = Hypervolume(minimum=[0,0,0], maximum=[1,1,1])

# initialize dictionary to hold hypervolume results
results = {}
for algorithm in algorithms:
    # store the hypervolume result with the algorithm's name as the key
    results[algorithm.__class__.__name__] = hyp(algorithm.result)

# sort the results in descending order based on hypervolume
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

# print the sorted results
for i, (name, hv) in enumerate(sorted_results, 1):
    print("No.%d: %s " % (i, name))
    print("      Hypervolume: %0.3f" % hv)


from mpl_toolkits.mplot3d import axes3d
# increase figure size# incre
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)

# generate the plot
for i in range(len(algorithms)):
    fig = plt.figure()  # create a new figure for each algorithm
    s = algorithms[i].result
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.scatter([s.objectives[0] for s in algorithms[i].result],
               [s.objectives[1] for s in algorithms[i].result],
               [s.objectives[2] for s in algorithms[i].result])
    ax.set_xlim([0, 1.1])
    ax.set_ylim([0, 1.1])
    ax.set_zlim([0, 1.1])
    ax.view_init(elev=30.0, azim=15)
    ax.set_title(algorithms[i].__class__.__name__)

    # save each figure in the same directory as a separate png file
    plt.savefig(algorithms[i].__class__.__name__ + '.png')

    plt.close(fig)  # close the figure after saving to free up memory

plt.show()
