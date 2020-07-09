maze=[[1,2,3],[1,2,3],[1,2,3]]
for i in range(len(maze)):
    row = int(i / len(maze))
    col = int(i %len(maze))
    print(maze[row][col])

