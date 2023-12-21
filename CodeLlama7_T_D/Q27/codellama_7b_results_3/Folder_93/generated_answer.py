
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    index = my_list.index(54) + 1 # find the index of 54 and add 1 to it
    new_list.insert(index, [54, 13]) # insert [54, 13] at the found index
    return new_list
