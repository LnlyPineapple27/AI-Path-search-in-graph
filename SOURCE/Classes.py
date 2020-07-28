import sys
# ----------------------------------Data processing-----------------------
class Node:    
    def __init__(self, num: int, line_data: str):
        self.number = num
        if line_data:
            self.near_by = [int(i) for i in line_data.split(" ")]
            self.near_by.sort()
            
    def __str__(self):
        line = str()
        line += "NUM: " + str(self.number)
        line += "\nNEAR BY: " + str(self.near_by) + "\n\n"
        return line
    
    def adjacent_list(self):
        return self.near_by
    
    
class Maze:
    def __init__(self, size: int, node_list: list, goal):
        if (size > 0) and node_list:
            self.size = size
            self.goal = goal
            self.goal_col_heuristic = int(goal) // self.size           
            self.goal_row_heuristic = int(goal) % self.size
            self.board = []
            count = 0
            for row in range(0,self.size):
                data = []
                for col in range(0,self.size):
                    data.append(Node(count, node_list[count]))
                    count += 1
                self.board.append(data)             
        else:
            print("[Error]: Invalid input while initializing Maze class object")
            sys.exit()
            
                 
    def printOut(self):
        for row in range(self.size):
            for col in range(self.size):
                print("col: {0} - row: {1} -> {2}".format(row,col,self.board[row][col]))
    
    def getNode(self, num: int):
        if((num >= 0) and (num < (self.size * self.size))):
            # quotient = num // size -> col x
            # remainder = num % size -> row y
            return self.board[num // self.size][num % self.size]                
        else:
            return None
        
    def getSize(self):
        return self.size
    
    def manhattan_heuristic_calculator(self, node):    
        curr_col = int(node) // self.size
        curr_row = int(node) % self.size        
        manhattan_distance = abs(curr_col - self.goal_col_heuristic) + abs(curr_row - self.goal_row_heuristic)    
        return manhattan_distance

def getLocationinMaze(num: int, size: int):
    if num >= 0 and size > 0:        
        # quotient = num // size -> col x
        # remainder = num % size -> row y
        return (num // size), (num % size)
    else:
        print("Invalid input")
        return None

#-----------------------------------Frontier processing------------------

def is_in_frontier(node, frontier):
    for i in range(len(frontier)):
        temp = frontier[i]
        if temp["Node"] == node:
            return i
    return None

def ExploreFrontier(frontier_list):
    # this function will determine the node with lowest cost and number order to be explored next
    if frontier_list:
        possible_choice = []
        # a large random number is chosen for later comparison to get minimum value
        min = 99999*9999999

        for item in frontier_list:
            cur_cost = item["Cost"]
            if cur_cost < min: # if a shorter cost is found, update possible_path and min value
                min = cur_cost
                possible_choice.clear()
                possible_choice.append(item)
            elif cur_cost == min: # found another possible path with the same minimum cost
                possible_choice.append(item)
        if len(possible_choice) > 1:
            possible_choice = sorted(possible_choice, key = lambda i: i['Node']) # bring the path with lower number order to the top
            print(possible_choice)
        best_result = possible_choice[0]
        frontier_list.remove(best_result) # remove the best result from frontier before exploring it
        return best_result
    return None

# -----------------------------------------------------
def tracePath(list_of_dict, start, goal): # list_of_dict must be valid to give correct result
    path = []
    tracing = goal
    if list_of_dict:
        for i in range(len(list_of_dict), 0, -1):
            if tracing is None:
              break
            cur = list_of_dict[i - 1]
            if cur["Node"] == tracing:
                path.append(cur["Node"])
                tracing = cur["Parent"]
                if cur["Node"] == start:
                    break
    path.reverse()# to get path from start to goal
    return path