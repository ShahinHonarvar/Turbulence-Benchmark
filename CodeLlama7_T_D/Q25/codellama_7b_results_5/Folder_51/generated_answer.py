
def insert_at_index(my_list):
    new_list = my_list[:] # make a copy of the original list
    new_list.insert(19, 249.61) # insert the value at index 19
    return new_list # return the modified list
