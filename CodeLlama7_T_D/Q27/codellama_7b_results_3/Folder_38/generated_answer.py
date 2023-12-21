
def insert_after_index(my_list):
    new_list = my_list[:] # create a shallow copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 89: # find the index where we want to insert the element
            new_list.insert(i + 1, 86) # insert the element at the next index
    return new_list
