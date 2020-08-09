#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# grid = []
# grid.append([3,0,6,5,0,8,4,0,0])
# grid.append([5,2,0,0,0,0,0,0,0])
# grid.append([0,8,7,0,0,0,0,3,1])
# grid.append([0,0,3,0,1,0,0,8,0])
# grid.append([9,0,0,8,6,3,0,0,5])
# grid.append([0,5,0,0,9,0,6,0,0])
# grid.append([1,3,0,0,0,0,2,5,0])
# grid.append([0,0,0,0,0,0,0,7,4])
# grid.append([0,0,5,2,0,6,3,0,0])

integers = range(1,10)

def check_value(grid,value,row_index,column_index):
    # checks an invididual value - true if fits in grid
    if value in grid[row_index]:
        return False
    elif value in [row[column_index] for row in grid]:
        return False
    elif value in cube_list(grid,get_cube(row_index,column_index)):
        return False
    return True

def get_cube(row_index,column_index):
    """
    grid:
        012
        345
        678
    """
    cube = row_index//3*3 + column_index//3
    return cube

def cube_list(grid,cube):
    l = [] 
    for row_index, row in enumerate(grid):
        for column_index, value in enumerate(row):
            if get_cube(row_index,column_index) == cube:
                l.append(value)
    return set(l)

def generate_options(grid,row_index,column_index):
    # checks possible integers and returns options
    options = []
    for i in integers:
        if check_value(grid,i,row_index,column_index):
            options.append(i)
    return options
        
def solve(grid):
    for row_index, row in enumerate(grid):
        for column_index, val in enumerate(row):
            if val == 0:
                options = generate_options(grid,row_index,column_index)
                if len(options) > 0:
                    for o in options:
                        temp_grid = grid[:]
                        temp_grid[row_index][column_index] = o
                        solution = solve(temp_grid)
                        if solution == False:
                            continue
                        return solution
                grid[row_index][column_index] = 0
                return False
            else:
                next
    print("Solved!")
    for row in grid:
        print(row)
    return grid

            
    
                    

