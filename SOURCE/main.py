"""
 Name:  Phan Tấn Đạt
 ID:    18127078
 Email: 18127078@student.hcmus.edu.vn
 AI lab01 Project
"""
from BFS import BFS_Search
from Classes import Maze
from timeit import default_timer as timer

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

def OutputData(file_dir: str, algorithm_name: str, time, expanded, path):
    file_dir += (algorithm_name + ".txt")
    file = open(file_dir, "w")
    file.write(algorithm_name)
    file.write("\nTime: " + str(time) + " ms")
    file.write("\nExpanded list:\t" + str(expanded))
    file.write("\nPath found:\t" + str(path))

    file.close()


# =====================================================
input_list = ImportData("..\INPUT\data.txt")
if not input_list:
    print("No data was imported")

size = int(input_list.pop(0))
goal = int(input_list.pop(-1))
board = Maze(size,input_list,goal)

# ------------------------
start = timer()

res = BFS_Search(board, 46, 6)
end = timer()
# The default_timer returns the time in microsecond -> *1000 to get milisec
Timer = (end - start)*1000 
if res == None:
    print("Can't find any possible path :(")
elif res == ([],[]):
    print("The goal is at starting point")
else:
    print(res)
    OutputData("..\OUTPUT\ ","BFS", Timer, res[0], res[1])
