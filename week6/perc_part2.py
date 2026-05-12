"""
Filename: perc_part2.py
Author: Aidan Stoaks
Date: May 11, 2026
Assignment: Project 3, Percolation Part 2
Collaborators: DU Comp Sci Dept.

This project focusses on spread probability in multiple forests, instead of in one forest
"""
from perc_part1 import Forest, Cell

class FireProbability:
    def __init__(self):
        pass

    def probability_Of_fire_spread_bfs(self, d: float) -> float:
        """
        Calculates the relative probablity of a fire spreading in a forest of density "d", uses a breadth first search

        Args:
            d: density of the forest, a float value

        Returns:
            float: The calculated probability of a fire spreading in the forest of density "d"
        """
        fire_spread_count = 0

        for i in range(1000):
            f = Forest(20, 20, d)
            if f.bfs():
                fire_spread_count += 1

        # probability that fire will spread in forests of density "d"
        return float(f'{fire_spread_count / 1000:.3f}') 
    
    def probability_of_fire_spread_dfs(self, d: float) -> float:
        """
        Calculates the relative probablity of a fire spreading in a forest of density "d", uses a depth first search

        Args:
            d: density of the forest, a float value

        Returns:
            float: The calculated probability of a fire spreading in the forest of density "d"
        """
        fire_spread_count = 0

        for i in range(1000):
            f = Forest(20, 20, d)
            if f.dfs():
                fire_spread_count += 1

        # probability that fire will spread in forests of density "d"
        return float(f'{fire_spread_count / 1000:.3f}')

    def highest_Density_bfs(self) -> float:
        """
        Calculates the maximum density possible to give a probability of 0.5 for fire spread in forests using a binary search and breadth first search

        Returns:
            float: the value "d" which gives a probability of 0.5 for forest fire spread
        """
        low_density = 0.0
        high_density = 1.0
        density = 0

        for i in range(20):
            # check midpoint
            density = (high_density + low_density) / 2

            # calculate probability at each density
            p = self.probability_Of_fire_spread_bfs(density)

            # check probability against threshold
            if p < 0.5:
                # prob is low, increase density
                low_density = density
            else:
                # high prob, decrease density
                high_density = density
        
        # last density value is what we seek
        return density
    
    def highest_Density_dfs(self) -> float:
        """
        Calculates the maximum density possible to give a probability of 0.5 for fire spread in forests using a binary search and depth first search

        Returns:
            float: the value "d" which gives a probability of 0.5 for forest fire spread
        """
        low_density = 0.0
        high_density = 1.0
        density = 0

        for i in range(20):
            # check midpoint
            density = (high_density + low_density) / 2

            # calculate probability at each density
            p = self.probability_of_fire_spread_dfs(density)

            # check probability against threshold
            if p < 0.5:
                # prob is low, increase density
                low_density = density
            else:
                # high prob, decrease density
                high_density = density
        
        # last density value is what we seek
        return density

def main():
    FP = FireProbability()
    highest_dfs = FP.highest_Density_dfs()
    highest_bfs = FP.highest_Density_bfs()

    print(f'Highest Density DFS: {highest_dfs}')
    print(f'Highest Density BFS: {highest_bfs}')
    print(f'Check prob of DFS density: {FP.probability_of_fire_spread_dfs(highest_dfs)}')
    print(f'Check prob of BFS density: {FP.probability_Of_fire_spread_bfs(highest_bfs)}')

if __name__ == '__main__':
    main()
