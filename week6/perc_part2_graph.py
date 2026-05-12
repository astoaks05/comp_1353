"""
Filename: perc_part2_graph.py
Author: Aidan Stoaks
Date: May 11, 2026
Assignment: Project 3, Percolation Part 2, Graph
Collaborators: DU Comp Sci Dept.

This project graphs density versus probability of spread using mmatplotlib
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
from perc_part2 import FireProbability

def generate_graph():
    """
    Plots a graph of the densities versus fire spreading probability of both dfs and bfs methods in the FireProbability class. Bfs shown in red, Dfs in orange. 
    """
    # going to graph densities as x coord and probabilities as the y coord
    densities_bfs = []
    densities_dfs = []
    probabilities_bfs = []
    probabilities_dfs = []

    # increment densities by 0.01, starting at 0.0
    FP = FireProbability()
    density = 0.0
    while density <= 1.0:
        # append the densities to each list
        densities_bfs.append(density)
        densities_dfs.append(density)

        # calculate probabilities of each density
        prob_bfs = FP.probability_Of_fire_spread_bfs(density)
        prob_dfs = FP.probability_of_fire_spread_dfs(density)

        # append probabilities to each list
        probabilities_bfs.append(prob_bfs)
        probabilities_dfs.append(prob_dfs)

        # Increment by 0.01 (using round to avoid floating point math errors)
        density = round(density + 0.01, 2)

    # plot bfs in red, and dfs in orange
    plt.plot(densities_bfs, probabilities_bfs, color='red')
    plt.plot(densities_dfs, probabilities_dfs, color='orange')
    plt.xlabel('Forest density')
    plt.ylabel('Probability of fire spread')

    plt.xlim(0, 1.0)
    plt.ylim(0, 1.05)
    
    # Set major ticks (with labels) at 0.2 intervals
    plt.xticks(np.arange(0, 1.2, 0.2))
    plt.yticks(np.arange(0, 1.2, 0.2))
    
    # Set minor ticks (without labels) at 0.01 intervals
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(0.01))
    ax.yaxis.set_minor_locator(MultipleLocator(0.01))
    
    plt.grid(True, alpha=0.3, which='minor')
    plt.show()

def main():
    generate_graph()

if __name__ == '__main__':
    main()


