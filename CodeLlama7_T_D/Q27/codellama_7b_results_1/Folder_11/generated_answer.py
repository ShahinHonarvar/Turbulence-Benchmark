
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 40:
            new_list.insert(i+1, 169.26) # insert the value at the next index
    return new_list
