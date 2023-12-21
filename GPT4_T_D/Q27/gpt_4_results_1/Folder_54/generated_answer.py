
def insert_after_index(my_list):
    if 43 in my_list:
        index_43 = my_list.index(43)
        my_list.insert(index_43 + 1, 37)
    return my_list
