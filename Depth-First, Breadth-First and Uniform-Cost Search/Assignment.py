# Student Name: Ismail Ulas Bayram
# Student ID: 220201040

from random import randint

# Our maze
maze = [[0,0,1,0,1],
        ["-","-",2,1,2],
        [2,"-",3,0,"-"],
        [0,2,1,1,"-"],
        [1,0,3,1,"-"]]

init = [0,0]
goal = [4,2]

def breadth_first_search(maze,init,goal):
    row, column = len(maze), len(maze[0])
    explored = []
    frontier = []
    frontier.append(init)
    x,y = init
    cost = 0 # path cost
    while(goal[0] != x or goal[1] != y):

        if(len(frontier) == 0): # If frontier is empty
            return False

        x,y = frontier.pop(0) # I use the list as if queue. I pop first element.
        explored.append([x, y]) # Before determining the frontiers, I append our node to explored set

        if (len(explored) == 1): # If the size of explored list is equal to 1, then there must not be no movement.
            cost = 0
        else:
            cost += 1

        # Below that, movement scenarios is generated with boundries. Movement points must be inside the our maze and
        # our movement must not be inside explored and frontier list. After that, if movement is available, then
        # I add next tiles into frontier list.
        if (0 <= x < row and 0 <= y - 1 < column and isinstance(maze[x][y - 1], int) and (
            [x, y - 1] not in explored) and ([x, y - 1] not in frontier)):
            frontier.append([x, y - 1])
        if (0 <= x - 1 < row and 0 <= y < column and isinstance(maze[x - 1][y], int) and (
            [x - 1, y] not in explored) and ([x - 1, y] not in frontier)):
            frontier.append([x - 1, y])
        if (0 <= x < row and 0 <= y + 1 < column and isinstance(maze[x][y + 1], int) and (
            [x, y + 1] not in explored) and ([x, y + 1] not in frontier)):
            frontier.append([x, y + 1])
        if (0 <= x + 1 < row and 0 <= y < column and isinstance(maze[x + 1][y], int) and (
            [x + 1, y] not in explored) and ([x + 1, y] not in frontier)):
            frontier.append([x + 1, y])

    print("Breadth First Search")
    print("Path --> " , explored , ", Cost --> ", cost)

def depth_first_search(maze,init,goal):
    row, column = len(maze), len(maze[0])
    explored = []
    frontier = []
    frontier.append(init)
    x, y = init
    cost = 0 # path cost
    while(goal[0] != x or goal[1] != y):

        if (len(frontier) == 0): # If frontier is empty
            return False

        x, y = frontier.pop() # I use the list as if stack. I pop end element of the list.
        explored.append([x, y]) # Before determining the frontiers, I append our node to explored set

        if(len(explored)==1): # If the size of explored list is equal to 1, then there must not be no movement.
            cost = 0
        else:
            cost += 1

        # Below that, movement scenarios is generated with boundries. Movement points must be inside the our maze and
        # our movement must not be inside explored and frontier list. After that, if movement is available, then
        # I add next tiles into frontier list.
        if (0 <= x < row and 0 <= y - 1 < column and isinstance(maze[x][y - 1], int) and (
            [x, y - 1] not in explored) and ([x, y - 1] not in frontier)):
            frontier.append([x, y - 1])
        if (0 <= x - 1 < row and 0 <= y < column and isinstance(maze[x - 1][y], int) and (
            [x - 1, y] not in explored) and ([x - 1, y] not in frontier)):
            frontier.append([x - 1, y])
        if (0 <= x < row and 0 <= y + 1 < column and isinstance(maze[x][y + 1], int) and (
            [x, y + 1] not in explored) and ([x, y + 1] not in frontier)):
            frontier.append([x, y + 1])
        if (0 <= x + 1 < row and 0 <= y < column and isinstance(maze[x + 1][y], int) and (
            [x + 1, y] not in explored) and ([x + 1, y] not in frontier)):
            frontier.append([x + 1, y])

    print("Depth First Search")
    print("Path --> ", explored, ", Cost --> ", cost)

def uniform_cost_search(maze,init,goal):
    row, column = len(maze), len(maze[0])
    flag = True # For ending while loop
    path_cost = 0
    explored, frontier = [], []
    explored_path, frontier_path = [], [] # At every iteration, I add elements the path lists as path with costs
    frontier_path.append([[init],path_cost])
    frontier.append(init)

    while(flag):

        if (len(frontier) == 0): # If frontier is empty
            return False

        count = list(i[1] for i in frontier_path) # To extract cost numbers
        min_cost = min(count) # To select minimum cost
        min_index = count.index(min_cost) # To determine which index of path has minimum cost
        path_with_cost = frontier_path.pop(min_index) # By using index number, we select the path
        path = path_with_cost[0]
        path1, path2, path3, path4 = path.copy(),path.copy(),path.copy(),path.copy()
        path_cost = path_with_cost[1] # Path cost of selected path
        x,y = path[len(path)-1]
        explored.append([x, y])

        # Below that, movement scenarios is generated with boundries. Movement points must be inside the our maze and
        # our movement must not be inside explored and frontier list. After that, if movement is available, then
        # I add next tiles into frontier list and next path and path cost into the frontier path list.
        if (0 <= x < row and 0 <= y - 1 < column and isinstance(maze[x][y - 1], int) and (
                    [x, y - 1] not in explored) and ([x, y - 1] not in frontier)):
            path1.append([x,y-1])
            frontier_path.append([path1,path_cost+1])
            frontier.append([x,y-1])
        if (0 <= x - 1 < row and 0 <= y < column and isinstance(maze[x - 1][y], int) and (
                    [x - 1, y] not in explored) and ([x - 1, y] not in frontier)):
            path2.append([x - 1, y])
            frontier_path.append([path2, path_cost + 1])
            frontier.append([x-1,y])
        if (0 <= x < row and 0 <= y + 1 < column and isinstance(maze[x][y + 1], int) and (
                    [x, y + 1] not in explored) and ([x, y + 1] not in frontier)):
            path3.append([x, y + 1])
            frontier_path.append([path3, path_cost + 1])
            frontier.append([x,y+1])
        if (0 <= x + 1 < row and 0 <= y < column and isinstance(maze[x + 1][y], int) and (
                    [x + 1, y] not in explored) and ([x + 1, y] not in frontier)):
            path4.append([x + 1, y])
            frontier_path.append([path4, path_cost + 1])
            frontier.append([x+1,y])

        # If any path that reaches to goal tile, we add this to explored path list until frontier path list is empty.
        if(goal[0] == x and goal[1] == y):
            explored_path.append(path_with_cost)

        # If frontier path list is empty, then flag becomes false and while loop ends.
        if(not frontier_path):
            flag = False

    print("Uniform Cost Search")
    print("Path --> ", explored_path[0][0] , ", Cost --> " , explored_path[0][1])

def uniform_cost_search_with_move_points(maze,init,goal):
    row, column = len(maze), len(maze[0])
    flag = True # For ending while loop
    path_cost = 0
    explored, frontier = [], []
    explored_path, frontier_path = [], [] # At every iteration, I add elements the path lists as path with costs
    frontier_path.append([[init],path_cost])
    frontier.append(init)
    while(flag):

        if (len(frontier) == 0): # If frontier is empty
            return False

        count = list(i[1] for i in frontier_path) # To extract cost numbers
        min_cost = min(count) # To select minimum cost
        min_index = count.index(min_cost) # To determine which index of path has minimum cost
        path_with_cost = frontier_path.pop(min_index) # By using index number, we select the path
        path = path_with_cost[0]
        path1, path2, path3, path4 = path.copy(),path.copy(),path.copy(),path.copy()
        path_cost = path_with_cost[1] # Path cost of selected path
        x,y = path[len(path)-1]
        explored.append([x, y])

        # Below that, movement scenarios is generated with boundries. Movement points must be inside the our maze and
        # our movement must not be inside explored and frontier list. After that, if movement is available, then
        # I add next tiles into frontier list and next path and path cost with extra move point into the frontier path list.
        if (0 <= x < row and 0 <= y - 1 < column and isinstance(maze[x][y - 1], int) and (
                    [x, y - 1] not in explored) and ([x, y - 1] not in frontier)):
            path1.append([x,y-1])
            frontier_path.append([path1,path_cost+1+maze[x][y-1]])
            frontier.append([x,y-1])
        if (0 <= x - 1 < row and 0 <= y < column and isinstance(maze[x - 1][y], int) and (
                    [x - 1, y] not in explored) and ([x - 1, y] not in frontier)):
            path2.append([x - 1, y])
            frontier_path.append([path2, path_cost + 1+maze[x-1][y]])
            frontier.append([x-1,y])
        if (0 <= x < row and 0 <= y + 1 < column and isinstance(maze[x][y + 1], int) and (
                    [x, y + 1] not in explored) and ([x, y + 1] not in frontier)):
            path3.append([x, y + 1])
            frontier_path.append([path3, path_cost + 1+maze[x][y+1]])
            frontier.append([x,y+1])
        if (0 <= x + 1 < row and 0 <= y < column and isinstance(maze[x + 1][y], int) and (
                    [x + 1, y] not in explored) and ([x + 1, y] not in frontier)):
            path4.append([x + 1, y])
            frontier_path.append([path4, path_cost + 1+maze[x+1][y]])
            frontier.append([x+1,y])

        if(goal[0] == x and goal[1] == y):
            explored_path.append(path_with_cost)
        if(not frontier_path):
            flag = False

    print("Uniform Cost Search With Move Points")
    print("Path --> ", explored_path[0][0], ", Cost --> ", explored_path[0][1])

# This function is written for generating heuristic list by calculating Euclidean Distance for each point with respect to goal point.
def euclidean_distance_for_heuristic(maze,goal):
    heuristic_maze = []
    for x in range(0, len(maze)):
        heuristic_maze.append([])
        for y in range(0, len(maze[0])):
            euclidean_distance = round((sum((i - j) ** 2 for i, j in zip([x, y], goal)) ** 0.5))
            heuristic_maze[x].append(euclidean_distance)
    return heuristic_maze

# This function is written for A*-Search with inadmissable approach
# I multiply heuristic cost with 100 up to half of the total maze element
# e.g. our maze has 25 elements and I change 12 heuristic costs (25/2= 12.5 -> rounded -> 12)
def heuristic_with_inadmissable(maze,goal):
    heuristic_maze = euclidean_distance_for_heuristic(maze,goal)
    list_inadmissable = []
    inadmissable_num = round((len(maze)*len(maze[0]))/2)
    for i in range(inadmissable_num):
        x = randint(0, 4)
        y = randint(0, 4)
        if([x,y] not in list_inadmissable):
            list_inadmissable.append([x,y])

    for i in list_inadmissable:
        heuristic_maze[i[0]][i[1]] = heuristic_maze[i[0]][i[1]]*100

    return heuristic_maze

def a_star_search_with_admissable(maze,init,goal):
    row, column = len(maze), len(maze[0])
    flag = True # For ending while loop
    path_cost = 0
    explored, frontier = [], []
    explored_path, frontier_path = [], [] # At every iteration, I add elements the path lists as path with costs
    frontier_path.append([[init],path_cost,path_cost])
    frontier.append(init)

    heuristic_maze = euclidean_distance_for_heuristic(maze,goal) # For generating Heuristic maze with admissable approach

    while(flag):

        if (len(frontier) == 0): # If frontier list is empty
            return False

        count = list(i[1] for i in frontier_path) # To extract cost numbers
        min_cost = min(count) # To select minimum cost
        min_index = count.index(min_cost) # To determine which index of path has minimum cost
        path_with_cost = frontier_path.pop(min_index) # By using index number, we select the path
        path = path_with_cost[0]
        path1, path2, path3, path4 = path.copy(),path.copy(),path.copy(),path.copy()
        path_cost = path_with_cost[2]
        x,y = path[len(path)-1]
        explored.append([x, y])

        # Below that, movement scenarios is generated with boundries. Movement points must be inside the our maze and
        # our movement must not be inside explored and frontier list. After that, if movement is available, then
        # I add next tiles into frontier list and (1)next path and (2)path cost with extra move point plus
        # heuristic cost and (3)path cost with extra move point into the frontier path list.
        # For the next iteration, I select 3. element in list which is path cost with extra move point
        # Because, I do not use previous tile's heuristic for next tile's heuristic. To prevent this, I add
        # third element to the list without adding heuristic cost.
        if (0 <= x < row and 0 <= y - 1 < column and isinstance(maze[x][y - 1], int) and (
                    [x, y - 1] not in explored) and ([x, y - 1] not in frontier)):
            path1.append([x,y-1])
            frontier_path.append([path1,path_cost+1 + maze[x][y-1]+ heuristic_maze[x][y-1],path_cost + 1 + maze[x][y-1]])
            frontier.append([x,y-1])
        if (0 <= x - 1 < row and 0 <= y < column and isinstance(maze[x - 1][y], int) and (
                    [x - 1, y] not in explored) and ([x - 1, y] not in frontier)):
            path2.append([x - 1, y])
            frontier_path.append([path2, path_cost + 1 + maze[x-1][y] + heuristic_maze[x-1][y],path_cost + 1 + maze[x-1][y] ])
            frontier.append([x-1,y])
        if (0 <= x < row and 0 <= y + 1 < column and isinstance(maze[x][y + 1], int) and (
                    [x, y + 1] not in explored) and ([x, y + 1] not in frontier)):
            path3.append([x, y + 1])
            frontier_path.append([path3, path_cost + 1 + maze[x][y+1] + heuristic_maze[x][y+1],path_cost + 1 + maze[x][y+1]])
            frontier.append([x,y+1])
        if (0 <= x + 1 < row and 0 <= y < column and isinstance(maze[x + 1][y], int) and (
                    [x + 1, y] not in explored) and ([x + 1, y] not in frontier)):
            path4.append([x + 1, y])
            frontier_path.append([path4, path_cost + 1 + maze[x+1][y] + heuristic_maze[x+1][y],path_cost + 1 + maze[x+1][y]])
            frontier.append([x+1,y])

        if(goal[0] == x and goal[1] == y):
            explored_path.append(path_with_cost)
        if(not frontier_path):
            flag = False

    print("A* Search With Admissable")
    print("Path --> ", explored_path[0][0], ", Cost --> ", explored_path[0][1])

def a_star_search_with_inadmissable(maze,init,goal):
    row, column = len(maze), len(maze[0])
    flag = True # For ending while loop
    path_cost = 0
    explored, frontier = [], []
    explored_path, frontier_path = [], [] # At every iteration, I add elements the path lists as path with costs
    frontier_path.append([[init],path_cost,path_cost])
    frontier.append(init)

    heuristic_maze = heuristic_with_inadmissable(maze,goal) # For generating Heuristic maze with inadmissable approach

    while(flag):

        if (len(frontier) == 0): # If frontier list is empty
            return False

        count = list(i[1] for i in frontier_path) # To extract cost numbers
        min_cost = min(count) # To select minimum cost
        min_index = count.index(min_cost) # To determine which index of path has minimum cost
        path_with_cost = frontier_path.pop(min_index) # By using index number, we select the path
        path = path_with_cost[0]
        path1, path2, path3, path4 = path.copy(),path.copy(),path.copy(),path.copy()
        path_cost = path_with_cost[2]
        x,y = path[len(path)-1]
        explored.append([x, y])

        # Below that, movement scenarios is generated with boundries. Movement points must be inside the our maze and
        # our movement must not be inside explored and frontier list. After that, if movement is available, then
        # I add next tiles into frontier list and (1)next path and (2)path cost with extra move point plus
        # heuristic cost and (3)path cost with extra move point into the frontier path list.
        # For the next iteration, I select 3. element in list which is path cost with extra move point
        # Because, I do not use previous tile's heuristic for next tile's heuristic. To prevent this, I add
        # third element to the list without adding heuristic cost.
        if (0 <= x < row and 0 <= y - 1 < column and isinstance(maze[x][y - 1], int) and (
                    [x, y - 1] not in explored) and ([x, y - 1] not in frontier)):
            path1.append([x,y-1])
            frontier_path.append([path1,path_cost+1 + maze[x][y-1]+ heuristic_maze[x][y-1],path_cost + 1 + maze[x][y-1]])
            frontier.append([x,y-1])
        if (0 <= x - 1 < row and 0 <= y < column and isinstance(maze[x - 1][y], int) and (
                    [x - 1, y] not in explored) and ([x - 1, y] not in frontier)):
            path2.append([x - 1, y])
            frontier_path.append([path2, path_cost + 1 + maze[x-1][y] + heuristic_maze[x-1][y],path_cost + 1 + maze[x-1][y] ])
            frontier.append([x-1,y])
        if (0 <= x < row and 0 <= y + 1 < column and isinstance(maze[x][y + 1], int) and (
                    [x, y + 1] not in explored) and ([x, y + 1] not in frontier)):
            path3.append([x, y + 1])
            frontier_path.append([path3, path_cost + 1 + maze[x][y+1] + heuristic_maze[x][y+1],path_cost + 1 + maze[x][y+1]])
            frontier.append([x,y+1])
        if (0 <= x + 1 < row and 0 <= y < column and isinstance(maze[x + 1][y], int) and (
                    [x + 1, y] not in explored) and ([x + 1, y] not in frontier)):
            path4.append([x + 1, y])
            frontier_path.append([path4, path_cost + 1 + maze[x+1][y] + heuristic_maze[x+1][y],path_cost + 1 + maze[x+1][y]])
            frontier.append([x+1,y])

        if(goal[0] == x and goal[1] == y):
            explored_path.append(path_with_cost)
        if(not frontier_path):
            flag = False

    print("A* Search With Inadmissable")
    print("Path --> ", explored_path[0][0], ", Cost --> ", explored_path[0][1])


breadth_first_search(maze,init,goal)
print("----------------------------------------------------------------------------")
depth_first_search(maze,init,goal)
print("----------------------------------------------------------------------------")
uniform_cost_search(maze,init,goal)
print("----------------------------------------------------------------------------")
uniform_cost_search_with_move_points(maze,init,goal)
print("----------------------------------------------------------------------------")
a_star_search_with_inadmissable(maze,init,goal)
print("----------------------------------------------------------------------------")
a_star_search_with_admissable(maze,init,goal)
