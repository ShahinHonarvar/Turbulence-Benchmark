
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    index = my_list.index(96) + 1 # find the index of 96 and add 1 to it
    new_list.insert(index, 36) # insert 36 at the found index
    return new_list # return the modified list
