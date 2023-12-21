
def insert_after_index(my_list):
    new_list = my_list[:]
    index_of_427 = my_list.index(427)
    new_list.insert(index_of_427 + 1, [312, 441])
    return new_list
