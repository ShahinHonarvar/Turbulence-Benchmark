
def insert_after_index(my_list):
    index_56 = my_list.index(56)
    new_list = my_list[:index_56+1] + [54] + my_list[index_56+1:]
    return new_list
