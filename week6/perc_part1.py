"""
Filename: perc_part1.py
Author: Aidan Stoaks
Date: May 5, 2026
Assignment: Project 3, Percolation Part 1
Collaborators: DU Comp Sci Dept.

This project will create forests of different densities, and model the spread of forest fires within them.  By running many simulations, we can come up with an approximate probability of fire spreading 
"""
import dudraw
import random
from stacks_queues import Queue as Q

dudraw.set_canvas_size(500,500)

class Cell:
    def __init__(self, row: int, col: int):
        """
        Construct a cell class which holds its row and col value inside the grid

        Args:
            row: int
            col: int
        
        Returns: 
            None
        """
        self.row = row
        self.col = col

# Depth first search and Breadth first search
class Forest:
    def __init__(self, width: int, height: int, d: float):
        """
        Constructs a Forest class, which holds the grid, a 2D array showing where trees are in the forest, as well as the density, height, and width of the grid

        Args:
            width: int
            height: int
            d: float
        
        Returns:
            None
        """
        self.width = width
        self.height = height
        self.d = d
        self.grid = []
        for r in range(height):
            row = []
            for c in range(width):
                # use the density to determine if a tree should go there
                if random.random() < d:
                    # tree
                    row.append(1)
                else:
                    # no tree
                    row.append(0)
            self.grid.append(row)

    def __str__(self):
        """
        Prints a string representation of the forest grid

        Args: 
            None

        Returns:
            res: string
        """
        res = ''
        for r in self.grid:
            for c in r:
                res += f'{c}, '
            res += '\n'
        return res

    def draw(self):
        """
        Draws a visual representation of the Forest grid, green for trees, red for fire, and grey for no tree or fire

        Args:
            None
        
        Returns: 
            None
        """
        dudraw.set_x_scale(0, self.width)
        dudraw.set_y_scale(0, self.height)
        radius = 0.45
        for r in range (len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == 1:
                    dudraw.set_pen_color(dudraw.GREEN)
                elif self.grid[r][c] == 2:
                    dudraw.set_pen_color(dudraw.RED)
                else:
                    dudraw.set_pen_color(dudraw.GRAY)
                dudraw.filled_square(c+radius, (self.height - r - 1) + radius, radius)
        dudraw.show(175)

    def dfs(self):
        """
        Performs a depth first search on the Forest grid, to simulate Forest fire spreading. If the fire reaches the bottom (can only spread left, right, up, or down) then the fire spreads. Or else, the fire does not spread

        Args: 
            None

        Returns: 
            bool
        """
        # set the first row on fire
        cells_to_explore = []
        for c in range(self.width):
            # if tree in the first row, set it on fire >:)
            if self.grid[0][c] == 1:
                self.grid[0][c] = 2 # mark on fire
                cells_to_explore.append(Cell(0, c))
        
        # check for current cell reaching the bottom
        while len(cells_to_explore) != 0:
            cur_cell = cells_to_explore.pop()
            self.draw()
            # if the current cell is in the last row, return true
            if cur_cell.row == self.height-1:
                return True
            
            # check all four surrounding cells, set on fire if they are trees, making sure to not get any Index errors
            # check down first, and if there are no trees then move laterally and finally upwards
            if (cur_cell.row + 1) < self.height and self.grid[cur_cell.row + 1][cur_cell.col] == 1:
                self.grid[cur_cell.row + 1][cur_cell.col] = 2
                cells_to_explore.append(Cell(cur_cell.row + 1, cur_cell.col))
            else:
                # create neighbors list containing the indices of each neighbor of the current cell
                neighbors = [
                    (cur_cell.row, cur_cell.col - 1), #left
                    (cur_cell.row, cur_cell.col + 1), #right
                    (cur_cell.row - 1, cur_cell.col) #up
                ]
                
                for r, c in neighbors:
                    # if the row exists in the grid, and the col exists in the grid
                    if 0 <= r < self.height and 0 <= c < self.width:
                        # set the trees on fire, and put them on the stack
                        if self.grid[r][c] == 1:
                            self.grid[r][c] = 2
                            cells_to_explore.append(Cell(r, c))

        return False

    def bfs(self):
        """
        Performs a breadth first search on the Forest grid, to simulate Forest fire spreading. If the fire reaches the bottom (can only spread left, right, up, or down) then the fire spreads. Or else, the fire does not spread

        Args: 
            None

        Returns: 
            bool
        """
        cells_to_explore = Q()
        for c in range(self.width):
            # if tree in the first row, set it on fire >:)
            if self.grid[0][c] == 1:
                self.grid[0][c] = 2 # mark on fire
                cells_to_explore.enqueue(Cell(0, c))

        while len(cells_to_explore) != 0:
            cur_cell = cells_to_explore.dequeue()
            self.draw()
            if cur_cell.row == self.height - 1:
                return True
            
            # Check ALL neighbors equally
            neighbors = [
                (cur_cell.row + 1, cur_cell.col),  # down
                (cur_cell.row, cur_cell.col + 1), # right
                (cur_cell.row, cur_cell.col - 1), # left
                (cur_cell.row - 1, cur_cell.col)  # up
            ]
            
            for r, c in neighbors:
                if 0 <= r < self.height and 0 <= c < self.width:
                    if self.grid[r][c] == 1:
                        self.grid[r][c] = 2
                        cells_to_explore.enqueue(Cell(r, c))
        return False

def main():
    """
    Creates two Forests, completes a dfs on the first, and a bfs on the second
    
    Args: 
        None

    Returns: 
        None
    """
    forest1 = Forest(15, 15, 0.75)
    print(forest1.dfs())

    forest2 = Forest(15, 15, 0.75)
    print(forest2.bfs())

if __name__ == '__main__':
    main()

