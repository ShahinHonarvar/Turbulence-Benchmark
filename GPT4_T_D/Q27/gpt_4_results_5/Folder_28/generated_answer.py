
def insert_after_index(list_arg):
    index_74 = list_arg.index(74)
    new_list = list_arg[:]
    new_list.insert(index_74+1, 49)
    return new_list
