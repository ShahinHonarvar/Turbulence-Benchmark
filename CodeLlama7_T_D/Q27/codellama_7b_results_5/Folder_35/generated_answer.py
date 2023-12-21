
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    index = 100 # find the index where we want to insert the element
    new_list.insert(index + 1, [876, 203]) # insert the element at the next index after the given index
    return new_list # return the modified list
