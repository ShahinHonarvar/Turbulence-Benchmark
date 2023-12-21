
def insert_at_index(my_list):
    new_list = my_list[:] # create a shallow copy of the list
    new_list.insert(28, 717.02) # insert the value at index 28
    return new_list # return the modified list
