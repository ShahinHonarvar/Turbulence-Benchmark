
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    for i in range(len(my_list)):
        if my_list[i] == 32:
            new_list.insert(i+1, [54, 96])
    return new_list
