from heapq import heappush, heappop


def a_star_algo(source, dest, grid):

    # Heuristic function which calculates euclidian distance between nodes
    def heur_func(n):
        return ((n[0] - dest[0]) ** 2 + (n[1] - dest[1]) ** 2) ** 0.5

    # Function to get the nearest neighbors for a given node
    def get_node(coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return filter(check_node, neighbors)

    # Function to check whether a coordinate is valid one and is not an obstacle
    def check_node(coord):
        x, y = coord
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1

    cost_for_node = []
    heappush(cost_for_node, (0, source))
    arrival_point = {source: None}
    inter_cost = {source: 0}
    while cost_for_node:
        present_cost, present_node = heappop(cost_for_node)
        if present_node == dest:
            break
        for neighbor in get_node(present_node):
            new_cost = inter_cost[present_node] + 1
            if neighbor not in inter_cost or new_cost < inter_cost[neighbor]:
                inter_cost[neighbor] = new_cost
                total_cost = new_cost + heur_func(neighbor)
                heappush(cost_for_node, (total_cost, neighbor))
                arrival_point[neighbor] = present_node
    if dest not in arrival_point:
        return None

    path = []
    node = dest
    while node != source:
        path.append(node)
        node = arrival_point[node]
    path.append(source)
    path.reverse()
    return path


# Giving the n x n grid of the garden
# maze_size = int(input("Enter the dimensions of garden : "))
# maze = []
# for i in range(maze_size):
#     li = []
#     print(f"Enter values of row-{i+1}")
#     for j in range(maze_size):
#         ele=int(input())
#         li.append(ele)
#     maze.append(li)
# print("Given Maze Garden:")
# for i in range(maze_size):
#     for j in range(maze_size):
#         print(maze[i][j], end = " ")
#     print()
maze = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
print("Given Maze Garden: ")
for i in range(len(maze)):
    for j in range(len(maze)):
        print(maze[i][j],end=' ')
    print()
# Finding the coordinates where the flowers are present in the grid
main_points = list()
main_points.append((0, 0))
for i in range(len(maze)):
    for j in range(len(maze)):
        if maze[i][j] == 2:
            main_points.append((i, j))
main_points.append((6, 6))

# Finding the shortest path in the maze which collects all flowers
maze_path = []
for i in range(len(main_points) - 1):
    point = a_star_algo(main_points[i], main_points[i + 1], maze)
    # Since for every call for point we are starting with a coordinate
    # which is already recorded in the previous iteration
    # So we are deleting it from the list or else we will be getting duplicates
    # We can comment and do the following change in the last line as given
    # if(i>0):
    #     point.pop(0)
    maze_path += point

# Marking the path with special characters using the coordinates we got in the maze_path
for i in maze_path:
    maze[i[0]][i[1]] = '*'

# Printing the shortest path and the length of the shortest path
print("Shortest Path: ")
print(maze_path)
print("Traversal in Matrix: ")
for i in range(len(maze)):
    for j in range(len(maze)):
        print(maze[i][j], end =" ")
    print()
print("Shortest Path Length : ", len(maze_path)-2)
# If the pop is removed from the for loop then print length as len(maze_path)-(no.of iterations-1)
# There won't be any change in the Matrix Traversal as they are already marked as '*'
