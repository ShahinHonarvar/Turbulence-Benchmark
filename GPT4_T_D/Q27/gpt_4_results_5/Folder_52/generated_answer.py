
def insert_after_index(my_list):
    if 97 in my_list:
        idx = my_list.index(97)
        my_list.insert(idx + 1, 72.27)
    return my_list
