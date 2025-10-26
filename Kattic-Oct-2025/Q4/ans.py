rows, cols = map(int, input().split())
current = [x - 1 for x in map(int, input().split())]
end = [x - 1 for x in map(int, input().split())]

grid = []

for _ in range(rows):
    grid.append(list(map(str, input().split())))

def get_cell(grid, r, c, default=1):
    try:
        return int(grid[r][c])
    except IndexError:
        return default

while (True):

    if( current[0] == end[0] and current[1] == end[1] ):
        print(1)
        exit()

    grid[current[0]][current[1]] = "1";

    r, c = current[0], current[1]
    if ( get_cell(grid,r-1,c) == 0):
        current[0] -= 1
    elif (get_cell(grid,r,c+1) == 0):
        current[1] += 1
    elif (get_cell(grid,r+1,c) == 0):
        current[0] += 1
    elif ( get_cell(grid,r,c-1) == 0):
        current[0] -= 1
    else:
        print(0)
        exit()