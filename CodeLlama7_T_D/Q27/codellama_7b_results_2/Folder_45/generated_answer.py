
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    for i in range(len(new_list)):
        if i == 84: # check if index is equal to 84
            new_list.insert(i + 1, [13, 46]) # insert the new list at the next index after 84
    return new_list
