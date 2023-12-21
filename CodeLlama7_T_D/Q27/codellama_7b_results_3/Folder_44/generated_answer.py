
def insert_after_index(my_list):
    new_list = my_list[:]
    index = my_list.index(86, 77)
    new_list.insert(index + 1, [86, 77])
    return new_list
