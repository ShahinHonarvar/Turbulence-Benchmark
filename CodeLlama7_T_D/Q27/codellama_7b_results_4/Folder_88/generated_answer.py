
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    index_to_insert = my_list.index(91) + 1 # find the index where we want to insert the element
    new_list.insert(index_to_insert, [46, 13]) # insert the element at the specified index
    return new_list
