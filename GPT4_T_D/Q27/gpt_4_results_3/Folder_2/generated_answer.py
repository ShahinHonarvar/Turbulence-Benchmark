
def insert_after_index(my_list):
    if 427 in my_list:
        index = my_list.index(427)
        my_list.insert(index+1, [312, 441])
    return my_list
