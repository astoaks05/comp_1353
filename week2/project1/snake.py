'''
Snake game program
Author: Aidan Stoaks
Filename: snake.py
Date: 4/12/2026
Class: comp1353
Collaborators: DU Comp Sci Dept.
'''
from DoublyLinkedList import DoublyLinkedList as DLL
import dudraw
import random

dudraw.set_canvas_size(500, 500)
dudraw.set_x_scale(0, 20)
dudraw.set_y_scale(0, 20)
dudraw.clear(dudraw.LIGHT_GRAY)

class Apple:
    def __init__(self, val):
        # give apple starting position
        self.val = val

    def draw(self):
        '''
        Draws a red filled square to represent an apple

        Args: 
            None
        
        Returns:
            None
        '''
        dudraw.set_pen_color(dudraw.RED)
        x, y = self.val
        dudraw.filled_square(x, y, 0.5)

    def special_draw(self):
        '''
        Draws a yellow apple to represent a special apple

        Args: 
            None

        Returns:
            None
        '''
        dudraw.set_pen_color(dudraw.YELLOW)
        x, y = self.val
        dudraw.filled_square(x, y, 0.5)

    def move(self):
        '''
        Moves apples to random location on the board

        Args: 
            None

        Returns:
            None
        '''
        # place apple at random spot
        x, y = (random.randint(1, 19), random.randint(1, 19))
        self.val = (x, y)

    def special_move(self):
        '''
        Moves special apples to a location outside of view from the player

        Args:
            None

        Returns:
            None
        '''
        self.val = (25, 25)

class Snake:
    def __init__(self, length = 0):
        self.body = DLL()
        self.length = length

    def draw(self):
        '''
        Iterates through each body part and draws a square to represent it

        Args: 
            None
        
        Returns:
            None
        '''

        # draw the head differently 
        headx, heady = self.body.header.next.val
        dudraw.set_pen_color(dudraw.DARK_GREEN)
        dudraw.filled_square(headx, heady, 0.5)

        # loop through each body part
        cur = self.body.header.next.next
        while cur.next:
            x, y = cur.val
            dudraw.set_pen_color(dudraw.GREEN)
            dudraw.filled_square(x, y, 0.5)
            cur = cur.next

    def move(self, direction):
        '''
        Iterates through each body part and manipulates the center values accordingly, for the head the direction is needed, and the rest of the elements follow suit

        Args:
            direction: the direction the snake should be moving in 
        
        Returns:
            None
        '''
        # first make the body move
        cur = self.body.trailer.prev
        while cur != self.body.header.next:
            new_val = cur.prev.val
            cur.val = new_val
            cur = cur.prev

        # then make the head 
        head = self.body.header.next
        old_x, old_y = head.val
        if direction == 'left':
            # subtract 1 from x value of the head's center
            new_x = old_x - 1
            head.val = (new_x, old_y)
        elif direction == 'right':
            # add 1 to x value of the head's center
            new_x = old_x + 1
            head.val = (new_x, old_y)
        elif direction == 'down':
            # subtract 1 from y value of head's center
            new_y = old_y - 1
            head.val = (old_x, new_y)
        elif direction == 'up':
            # add 1 to y value of head's center
            new_y = old_y + 1
            head.val = (old_x, new_y)
    
    def eat_apple(self):
        '''
        Adds an element to the end of the snake body, and deletes the current apple / teleports the apple to a different spot

        Args:
            None
        
        Returns: 
            None
        '''
        self.body.add_last(self.body.trailer.prev.val)
        self.length += 1

    def eat_special_apple(self):
        '''
        Adds 3 elements to the end of the snake body, and deletes the current apple / teleports the apple to a different spot

        Args:
            None
        
        Returns: 
            None
        '''
        for i in range(3):
            self.body.add_last(self.body.trailer.prev.val)
        self.length += 3

limit = 10 # number of frames to allow to pass before snake moves
timer = 0  # a timer to keep track of number of frames that passed
snake = Snake()
apple = Apple((5, 10))
special_apple = Apple((25, 25))
# initialize the snake with three pieces
snake.body.add_first((15, 10))
snake.body.add_last((16,10))
snake.body.add_last((17,10))
# initialize key and direction and apple count
key = ''
direction = 'left'
apple_count = 0
special_apple_active = False
while True:
    timer += 1
    #process keyboard press here
    if key == 'a':
        direction = 'left'
    if key == 'd':
        direction = 'right'
    if key == 's':
        direction = 'down'
    if key == 'w':
        direction = 'up' 

    if timer == limit:
        timer = 0
        #draw snake and apple and move the snake
        dudraw.clear(dudraw.LIGHT_GRAY)
        apple.draw()
        snake.draw()
        
        # Only spawn special apple once per 5 apples eaten
        if apple_count > 0 and apple_count % 5 == 0 and not special_apple_active:
            special_apple.val = (random.randint(1, 19), random.randint(1, 19))
            special_apple_active = True
        
        if special_apple_active:
            special_apple.special_draw()

        snake.move(direction)
        #check to see if snake ate the fruits
        #check if the snake self intersects
        head = snake.body.header.next
        head_x, head_y = head.val
        cur = snake.body.header.next.next
        intersect = False
        while cur.next:
            if cur.val == head.val:
                intersect = True
            if cur.val == apple.val:
                snake.eat_apple()
                apple.move()
                apple_count += 1
            if cur.val == special_apple.val:
                snake.eat_special_apple()
                special_apple.special_move()
            cur = cur.next
        if intersect:
            break
        
        # check for wall collisions
        if head_x < 0 or head_x > 20 or head_y < 0 or head_y > 20:
            break

    key = dudraw.next_key_typed()
    dudraw.show(15)