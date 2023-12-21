
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 94: # check if the current element is 94
            new_list.insert(i+1, 93) # insert 93 at the next index after 94
    return new_list
