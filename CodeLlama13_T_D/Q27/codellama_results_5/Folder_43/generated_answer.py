
def insert_after_index(my_list):
    if 29 in my_list:
        index = my_list.index(29) + 1
        my_list.insert(index, [28, 53])
    return my_list
