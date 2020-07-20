"""
 Name:  Phan Tấn Đạt
 ID:    18127078
 Email: 18127078@student.hcmus.edu.vn
 AI lab01 Project
"""
#from BFS import BFS_Search

class Node:    
    def __init__(self, num: int, line_data: str):
        self.number = num
        if line_data:
            self.neighbors = [int(i) for i in line_data.split(" ")]
            
    def __str__(self):
        line = str()
        line += "NUM: " + str(self.number)
        line += "\nNEIGHBORS: " + str(self.neighbors) + "\n\n"
        return line   
        
class Maze:
    def __init__(self, size: int, node_list: list, goal: int):
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

                
class Coordinates:
    def __init__(self, x, y):
        self.col = x
        self.row = y
                
def getLocation(num: int, size: int):
    if num >= 0 and size > 0:        
        # quotient = num // size -> col x
        # remainder = num % size -> row y
        return Coordinates(num // size, num % size)
    else:
        print("Invalid input")
        
        
def ImportData(file_dir: str):
    # convert all lines from file to a list of strings
    data = []
    try:
        with open(file_dir) as file:
            for line in file:
                line = line.rstrip("\n")
                data.append(line)
                if 'str' in line:
                    break        
    except:
        print("No input file was found at given dir: "+ file_dir)
    finally:
        file.close()
        return data


# =====================================================
input_list = ImportData("..\INPUT\data.txt")
if not input_list:
    print("No data was imported")

size = int(input_list.pop(0))
goal = int(input_list.pop(-1))
board = Maze(size,input_list,goal)
# print("success")
board.printOut()

