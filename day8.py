'''
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves 
explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious 
if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need 
to count the number of trees that are visible from outside the grid when looking directly along a row or 
column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle 
input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the 
tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only 
consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no 
trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other 
    trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees 
    of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees 
    of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible 
in this arrangement.

Consider your map; how many trees are visible from outside the grid?
'''

### PART 1 ###
import numpy as np

# create grid using NumPy array
#grid = np.array([list(x.strip()) for x in open('sample_input.txt')], int)
grid = np.array([list(x.strip()) for x in open('day8_input.txt')], int)
#print(grid)

# find dimensions of grid
num_row, num_col = np.shape(grid)
#print(num_row)
#print(num_col)

# find count of outside edge of grid
count_edges = (num_row*2) + (num_col-2) * 2
#print(count_edges)

# set visible count to count of edge
count_visible = count_edges

# loop through inside trees
for i in range(1, num_row-1): #excludes top and bottom rows
    #print(grid[i])
    for j in range(1, num_col-1): #excludes left and right cols
        #print(grid[i][j])
        curr_tree = grid[i][j]
        trees_up = grid[:i, j] #compare trees up
        trees_down = grid[i+1:, j] #compare trees down
        trees_left = grid[i, :j] #compare trees left
        trees_right = grid[i, j+1:] #compare trees right
        #print(curr_tree)
        #print(trees_up)
        #print(trees_down)
        #print(trees_left)
        #print(trees_right)
       
        if curr_tree > max(trees_up) or curr_tree > max(trees_down) or curr_tree > max(trees_left) or curr_tree > max(trees_right):
            count_visible += 1
        else:
            continue

print(count_visible)


'''
--- Part Two ---

Content with the amount of tree cover available, the Elves just need to know the best spot to build their 
tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if 
you reach an edge or at the first tree that is the same height or taller than the tree under consideration. 
(If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house 
has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of 
    height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. 
For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?
'''

### PART 2 ###
tot_score = 0
best_score = 0

# loop through inside trees
for i in range(1, num_row-1): #excludes top and bottom rows
    #print(grid[i])
    for j in range(1, num_col-1): #excludes left and right cols
        #print(grid[i][j])
        curr_tree = grid[i][j]
        trees_up = grid[:i, j] #compare trees up
        trees_down = grid[i+1:, j] #compare trees down
        trees_left = grid[i, :j] #compare trees left
        trees_right = grid[i, j+1:] #compare trees right

        score_up = 0
        score_down = 0
        score_left = 0
        score_right = 0

        for x in range(len(trees_up)):
            score_up += 1
            if trees_up[len(trees_up) - 1 - x] >= curr_tree:
                break
        for x in range(len(trees_down)):
            score_down += 1
            if trees_down[x] >= curr_tree:
                break
        for x in range(len(trees_left)):
            score_left += 1
            if trees_left[len(trees_left) - 1 - x] >= curr_tree:
                break
        for x in range(len(trees_right)):
            score_right += 1
            if trees_right[x] >= curr_tree:
                break
        
        tot_score = score_up * score_down * score_left * score_right
        if tot_score > best_score:
            best_score = tot_score

print(best_score)
