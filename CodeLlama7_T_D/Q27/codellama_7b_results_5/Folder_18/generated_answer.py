
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 696: # find the index of the element to be inserted
            new_list.insert(i+1, 477) # insert the element at the next index
    return new_list
