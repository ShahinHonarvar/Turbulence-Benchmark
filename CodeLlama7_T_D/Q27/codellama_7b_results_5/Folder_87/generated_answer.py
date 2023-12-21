
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the input list
    for i in range(len(my_list)): # iterate over each element in the list
        if my_list[i] == 69: # check if the current element is equal to 69
            new_list.insert(i + 1, 92) # insert 92 at the next index after 69
    return new_list # return the modified list with 92 inserted at the appropriate index
