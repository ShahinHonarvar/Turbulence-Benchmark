
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(my_list)): # loop through the original list
        if i == 743: # check if we are at the index where we want to insert the element
            new_list.insert(i+1, 11.04) # insert the element at the next index
    return new_list
