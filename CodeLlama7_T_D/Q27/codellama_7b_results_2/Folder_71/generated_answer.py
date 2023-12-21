
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(my_list)): # iterate through the list
        if my_list[i] == 70: # check if we have reached the index of 70
            new_list.insert(i+1, 76) # insert 76 at the next index
    return new_list
