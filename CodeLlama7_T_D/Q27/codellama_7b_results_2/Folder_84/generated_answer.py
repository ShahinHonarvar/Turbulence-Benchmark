
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    index_to_insert = my_list.index(183) + 1 # find the index where to insert the value
    new_list.insert(index_to_insert, [148, 145]) # insert the value at the found index
    return new_list
