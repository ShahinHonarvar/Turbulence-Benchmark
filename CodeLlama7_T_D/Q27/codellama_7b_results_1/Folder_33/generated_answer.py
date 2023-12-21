
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the input list
    index_to_insert = my_list.index(556) + 1 # find the index where 974.0 should be inserted
    new_list.insert(index_to_insert, 974.0) # insert 974.0 at the found index
    return new_list
