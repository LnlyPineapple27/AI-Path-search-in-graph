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


class Evaluation:
    def __init__(self, cost, node_path):
        # cost = f(n) = h(n) + g(n)
        self.cost = cost
        self.path = node_path

    def getCost(self):
        return self.cost

    def getPath(self):
        return self.path

    def getFurthestNode(self):
        if self.path:
            return int(self.path[-1])
        return None

    def __str__(self):
        return "C: " + str(self.cost) + "- P: " + str(self.path)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

def getLocation(num: int, size: int):
    if num >= 0 and size > 0:
        # quotient = num // size -> col x
        # remainder = num % size -> row y
        return (num // size), (num % size)
    else:
        print("Invalid input")
        return None

#-----------------------------------Frontier processing------------------
def lastValue(path):
    return path[-1]

def ExploreFrontier(frontier_list):
    # this function will determine the node with lowest cost and number order to be explored next
    if frontier_list:
        possible_path = []
        # a large random number is chosen for later comparison to get minimum value
        min = 99999*9999999

        for item in frontier_list:
            cur_cost = item.getCost()
            if cur_cost < min: # if a shorter cost is found, update possible_path and min value
                min = cur_cost
                possible_path.clear()
                possible_path.append(item.getPath())
            elif cur_cost == min: # found another possible path with the same minimum cost
                possible_path.append(item.getPath())
        if len(possible_path) > 1:
            possible_path = sorted(possible_path, key = lastValue) # bring the path with lower number order to the top
            #print(possible_path)

        best_path = possible_path[0]
        res = Evaluation(min, best_path)
        frontier_list.remove(res) # remove the best result from frontier before exploring it
        return res

    return None

def is_in_frontier(node, frontier):
    for index in range(len(frontier)):
        item: Evaluation = frontier[index]
        path_item: list = item.getPath()
        if path_item[-1] == node:
            return index
    return None
