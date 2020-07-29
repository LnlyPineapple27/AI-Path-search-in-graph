import glob

def choose_input_files(dir):
    # ..\INPUT\
    file_list = glob.glob(dir + "\*.txt")
    if file_list:
        for i in range(len(file_list)):
            print("<" + str(i) + ">\t" + file_list[i])
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
                if line == "":
                    break
                data.append(line)
    except:
        print("No input file was found at given dir: "+ file_dir)

    return data

def printList(list_obj, seperator: str):
    res = ""
    for i in range(len(list_obj)):
        if i == 0:
            res += str(list_obj[i])
        else:
            res += (seperator + str(list_obj[i])) 
    return res

def OutputData(file_dir: str, algorithm_name: str, data):
    if len(data) == 2:          
        file_dir += (algorithm_name + ".txt")
        file = open(file_dir, "w")
        file.write(algorithm_name)
        
        if algorithm_name == "Iterative_deepening_search":
            
            expanded_by_depth = data[0]
            path = data[1]  
            if path is None:
                file.write(" unable to find any possible path!\nMaybe something went wrong :<")
                if expanded_by_depth is not None: 
                    count = 0
                    file.write("\n\tExpanded list:")
                    for i in range(len(expanded_by_depth)):
                        count += (len(expanded_by_depth[i]))
                        file.write("\n\t\tDepth = " + str(i)+ ": " + str(expanded_by_depth[i]))                   
                    file.write("\n\tTime to escape maze:\t\t" + str(count) + " minutes")
            else:        
                file.write("\n\tExpanded list:")
                count = 0
                for i in range(len(expanded_by_depth)):
                    count += (len(expanded_by_depth[i]))
                    file.write("\n\t\tDepth = " + str(i)+ ": " + str(expanded_by_depth[i]))                          
                file.write("\n\tPath found:\t\t" + printList(path,"->"))
                file.write("\n\tTime to escape maze:\t\t" + str(count) + " minutes")

        else:    
            expanded = data[0]
            path = data[1]  
            if path is None:
                file.write(" unable to find any possible path!\nMaybe something went wrong :<")
                if expanded is not None:                              
                    file.write("\n\tExpanded list:\t" + str(expanded))
                    file.write("\n\tTime to escape maze:\t\t" + str(len(expanded)) + " minutes")
            else:
                file.write("\n\tExpanded list:\t" + str(expanded))
                file.write("\n\tPath found:\t\t" + printList(path,"->"))
                file.write("\n\tTime to escape maze:\t\t" + str(len(expanded)) + " minutes")
        file.close()
        
def printResult(algorithm_name, data):   
    if len(data) == 2:    
        if algorithm_name == "Iterative_deepening_search":
            
            expanded_by_depth = data[0]
            path = data[1]  
            if path is None:
                print(algorithm_name + " unable to find any possible path!\nMaybe something went wrong :<")
                if expanded_by_depth is not None: 
                    count = 0
                    print("\tExpanded list:")
                    for i in range(len(expanded_by_depth)):
                        count += (len(expanded_by_depth[i]))
                        print("\t\tDepth = " + str(i)+ ": " + str(expanded_by_depth[i]))                  
                    print("\tTime to escape maze:\t\t" + str(count) + " minutes")
            else:        
                print("\n" + algorithm_name)
                print("\tExpanded list:")
                count = 0
                for i in range(len(expanded_by_depth)):
                    count += (len(expanded_by_depth[i]))
                    print("\t\tDepth = " + str(i)+ ": " + str(expanded_by_depth[i]))      
                    
                print("\tPath found:\t\t" + printList(path,"->"))
                print("\tTime to escape maze:\t\t" + str(count) + " minutes")

        else:    
            expanded = data[0]
            path = data[1]  
            if path is None:
                print(algorithm_name + " unable to find any possible path!\nMaybe something went wrong :<")
                if expanded is not None:                              
                    print("\tExpanded list:\t" + str(expanded))
                    print("\tTime to escape maze:\t\t" + str(len(expanded)) + " minutes")
            else:
                print("\n" + algorithm_name)
                print("\tExpanded list:\t" + str(expanded))
                print("\tPath found:\t\t" + printList(path,"->"))
                print("\tTime to escape maze:\t\t" + str(len(expanded)) + " minutes")
    
            