#sudoku solver making use of back tracking

#the input of the puzzle below can be changed
#if you have a puzzle that seems impossible to solve, you can just plug it in below :)
puzzle = [
    [0,0,0,0,9,0,0,2,0],
    [4,0,2,5,0,0,0,6,0],
    [0,5,3,0,7,0,0,4,0],
    [0,7,8,0,0,1,0,0,0],
    [9,0,0,0,5,0,0,0,0],
    [0,4,0,6,0,0,0,0,0],
    [0,0,0,0,0,7,0,0,2],
    [5,0,0,0,4,0,7,0,0],
    [0,0,0,0,0,0,1,0,6]
]


#checking if number fit in the position 
def possible(y, x, n):
    global puzzle
    for i in range(0,9):
        if puzzle[i][x] == n:     #for rows
            return False
    for i in range(0,9):
        if puzzle[y][i] == n:     #for columns
            return False

    x0 = (x//3)*3               #for squares
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if puzzle[y0+i][x0+j] == n:
                return False
    return True

#function to print the board out
def print_board(puzzle):
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(puzzle[0])):
            if j % 3 ==0 and j != 0:
                print(" | ", end="")

            if j ==8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")



#solving the puzzle
def solve():
    global puzzle
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):     #trying numbers from 1 - 9 to put in the empty blocks
                    if possible(y, x, n):  #checking if the number works
                        puzzle[y][x] = n   #number fits 
                        solve()            #continue solving
                        puzzle[y][x] = 0   #backtrack if the solution does not work
                return
    print_board(puzzle)                    #print the solution of the puzzle
    

#displaying puzzle and solution
print("PUZZLE:")
print_board(puzzle)
print(".............................")
print("SOLUTION:")
solve()



