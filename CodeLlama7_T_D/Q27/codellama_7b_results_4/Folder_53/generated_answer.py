
def insert_after_index(my_list):
    new_list = my_list[:] # make a copy of the list
    for i in range(len(new_list)):
        if i == 92:
            new_list.insert(i+1, 709.87)
    return new_list
