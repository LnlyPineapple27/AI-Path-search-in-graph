
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
        if (size > 0) and (goal >= 0) and (goal < (size * size)) and node_list:
            self.size = size
            self.goal = goal
            self.board = []
            count = 0
            for row in range(0,self.size):
                data = []
                for col in range(0,self.size):
                    data.append(Node(count, node_list[count]))
                    count += 1
                self.board.append(data)             
        else:
            print("[Error]: Invalid input")
                 
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


def getLocation(num: int, size: int):
    if num >= 0 and size > 0:        
        # quotient = num // size -> col x
        # remainder = num % size -> row y
        return (num // size), (num % size)
    else:
        print("Invalid input")
        return None
        
                