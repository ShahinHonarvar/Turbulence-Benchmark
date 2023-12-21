
def insert_after_index(my_list):
    if 66 in my_list:
        index_val = my_list.index(66)
        my_list.insert(index_val + 1, 45)
    return my_list
