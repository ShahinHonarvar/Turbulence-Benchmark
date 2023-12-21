
def insert_after_index(my_list):
    new_list = my_list[:] # create a shallow copy of the list
    index_of_four = my_list.index(4) # find the index of the element 4 in the list
    if index_of_four == len(my_list) - 1: # if the element 4 is the last element in the list
        new_list.append(7) # insert the element 7 at the end of the list
    else:
        new_list.insert(index_of_four + 1, 7) # insert the element 7 at the index immediately succeeding the index of element 4
    return new_list
