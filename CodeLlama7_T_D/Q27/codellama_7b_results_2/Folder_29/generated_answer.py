
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 96: # find the index where 36 should be inserted
            new_list.insert(i+1, 36) # insert 36 at the next index
    return new_list
