
def insert_after_index(my_list):
    new_list = my_list[:]
    index = new_list.index(761) + 1
    new_list.insert(index, 925)
    return new_list
