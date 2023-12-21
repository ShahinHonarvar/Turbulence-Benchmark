
def insert_after_index(my_list):
    new_list = my_list[:]
    index = my_list.index(30) + 1
    new_list.insert(index, 37)
    return new_list
