
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 57: # find the index of 57
            new_list.insert(i+1, 96) # insert 96 at the next index
    return new_list
