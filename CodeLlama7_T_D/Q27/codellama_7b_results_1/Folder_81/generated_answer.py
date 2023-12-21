
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 28: # find the index where we want to insert
            new_list.insert(i+1, 20) # insert the value at the next index
    return new_list
