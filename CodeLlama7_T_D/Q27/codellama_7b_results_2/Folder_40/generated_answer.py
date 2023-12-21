
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(my_list)):
        if i == 4:
            new_list.insert(i+1, 856.69)
    return new_list
