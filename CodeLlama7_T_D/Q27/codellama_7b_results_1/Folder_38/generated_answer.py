
def insert_after_index(my_list):
    new_list = my_list[:] # create a shallow copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 89: # find the index where 89 is located
            new_list.insert(i + 1, 86) # insert 86 at the next index after 89
    return new_list
