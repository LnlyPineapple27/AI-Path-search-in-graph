"""
 Name:  Phan Tấn Đạt
 ID:    18127078
 Email: 18127078@student.hcmus.edu.vn
 AI lab01 Project
"""
from Breadth_first_search import Breadth_first_search
from Uniform_cost_search import Uniform_cost_search
from Classes import Maze
from timeit import default_timer as timer
from file_tools import OutputData, ImportData, choose_input_files
import sys
# --------------------------------------
if __name__ == "__main__":
    file_name = choose_input_files("..\INPUT")
    
    if file_name is not None: 
        input_list = ImportData(file_name)
        if not input_list:
            print("No data was imported")
            sys.exit()
        size = int(input_list.pop(0))
        goal = int(input_list.pop(-1))
        board = Maze(size,input_list,goal)
               
        # start = input("Enter the number of starting point: ")
        # start = int(start)
        start = 0
        algorithms = [(Breadth_first_search), 
                      (Uniform_cost_search)]
        
        for method in algorithms:
            begin = timer()
            result = method(board, start, goal)
            end = timer()
            stopWatch = 1000 * (end - begin)
            print(method.__name__ + " completed\n")
            OutputData("..\OUTPUT\ ", method.__name__, stopWatch, result)
            
        