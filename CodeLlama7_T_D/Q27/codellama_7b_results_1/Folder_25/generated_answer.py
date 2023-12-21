
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 30: # find the index where we need to insert 37
            new_list.insert(i+1, 37) # insert 37 at the next index after 30
    return new_list
