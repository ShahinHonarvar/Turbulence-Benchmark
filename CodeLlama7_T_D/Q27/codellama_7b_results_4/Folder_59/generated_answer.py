
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    for i in range(len(my_list)): # iterate through the list
        if i == 9: # check if we have reached the index we want to insert at
            new_list.insert(i+1, 426.08) # insert the value at the next index
    return new_list
