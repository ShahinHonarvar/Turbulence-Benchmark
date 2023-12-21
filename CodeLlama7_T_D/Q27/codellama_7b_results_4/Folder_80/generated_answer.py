
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 95: # find the index of 95
            new_list.insert(i+1, 43) # insert 43 at the next index after 95
    return new_list
