import glob

def choose_input_files(dir):
    # ..\INPUT\
    file_list = glob.glob(dir + "\*.txt")
    if file_list:
        for i in range(len(file_list)):
            print(str(i) + ".\t" + file_list[i])
        while (1):
            get_choice = input("Input a GIVEN number to choose data file: ")
            choice = int(get_choice)
            if choice >= 0 and choice < len(file_list):
                return file_list[choice]           
    else:
        print("No input file was found in given directory!!!!")
        return None
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

    return data

def OutputData(file_dir: str, algorithm_name: str, time, data):
    expanded = data[0]
    path = data[1]
    file_dir += (algorithm_name + ".txt")
    file = open(file_dir, "w")
    file.write(algorithm_name)

    if expanded is None or path is None:
        file.write(" unable to find any possible path!\nMaybe something went wrong :<")
        file.write("\nRuntime: " + str(time) + " ms")      
        file.write("\nExpanded list:\t" + str(expanded))
    else:    
        file.write("\nRuntime: " + str(time) + " ms")
        file.write("\nExpanded list:\t" + str(expanded))
        file.write("\nPath found:\t" + str(path))
    
    file.close()
    
