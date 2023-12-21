
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    index_to_insert = next((i for i, x in enumerate(my_list) if x == 743), None) # find the index of the element to insert after
    if index_to_insert is not None: # check if the index was found
        new_list.insert(index_to_insert + 1, 11.04) # insert the element at the next index
    return new_list
