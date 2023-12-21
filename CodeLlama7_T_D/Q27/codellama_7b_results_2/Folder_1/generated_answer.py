
def insert_after_index(my_list):
    new_list = my_list[:]
    index = my_list.index(93) + 1
    new_list.insert(index, [33, 78])
    return new_list
