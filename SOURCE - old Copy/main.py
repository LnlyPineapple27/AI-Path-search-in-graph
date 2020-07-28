"""
 Name:  Phan Tấn Đạt
 ID:    18127078
 Email: 18127078@student.hcmus.edu.vn
 AI lab01 Project
"""
from Breadth_first_search import Breadth_first_search
from Uniform_cost_search import Uniform_cost_search
from Greedy_best_first_search import Greedy_best_first_search
from A_star_graph_search import A_star_graph_search

from Classes import Maze
from file_tools import OutputData, ImportData, choose_input_files, printResult
import sys
# --------------------------------------
if __name__ == "__main__":
    file_name = choose_input_files("..\INPUT")

    if file_name is not None:
        input_list = ImportData(file_name)
        if len(input_list) < 3:
            print("No data was imported")
            print(input_list)
            sys.exit()
        size = int(input_list.pop(0))
        goal = int(input_list.pop(-1))
        if (goal < 0) or (goal > int(size * size)):
            print("\n[Warning]: Goal doesn't exist in Maze!\n->This might result in long runtime and uncompleted result!!\n")
        board = Maze(size,input_list,goal)
        
        # start = input("Enter the number of starting point: ")
        # start = int(start)
        start = 0

        print("Starting point:\t", start)
        print("Goal:\t\t\t", goal)
        
        algorithms = [(Breadth_first_search),
                      (Uniform_cost_search),
                      (Greedy_best_first_search),
                      (A_star_graph_search)]

        for method in algorithms:
            result = method(board, start, goal)
            #print(method.__name__ + " completed\n")
            OutputData("..\OUTPUT\ ", method.__name__, result)
            printResult(method.__name__,result)

