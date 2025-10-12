import heapq
grid_info = list(map(int, input().split()))

cell_towers = {}
for i in range(1, grid_info[2] + 1): 
    cell_towers[i] = [x - 1 for x in map(int, input().split())]

rows, cols, towers = (grid_info[0]*2), grid_info[1], grid_info[2]
grid = [[0] * cols for _ in range(rows)]

for i in range(rows // 2):
    for j in range(cols):
        distances = [];
        for k in range(1, towers + 1):
            dist = abs(cell_towers[k][0] - i) + abs(cell_towers[k][1] - j)
            distances.append((dist, k))
        
        top2 = heapq.nsmallest(2, distances)
        
        grid[i][j] = top2[0][1]
        grid[i + rows // 2][j] = top2[1][1]

for row in grid:
    print(' '.join(map(str, row)))