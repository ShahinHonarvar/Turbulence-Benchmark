
def insert_after_index(my_list):
    new_list = my_list[:] # make a shallow copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 696:
            new_list.insert(i+1, 477) # insert 477 at index immediately succeeding 696
            break # no need to continue searching the list
    return new_list
