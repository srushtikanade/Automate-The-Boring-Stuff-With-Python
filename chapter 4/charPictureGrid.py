grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# here we have a 90 degree rotate, 8 rows become 8 columns, 0,0 to 8,5; now 0,0 to 5,8
for row in range(len(grid)): 
    for col in range(len(grid)):
        if col <8: # print 1st 7 column elements of that row w no spaces
            print(grid[col][row],end="")
        if col==8: #last column of that row so next elements in next line
            print(grid[col][row])
    


