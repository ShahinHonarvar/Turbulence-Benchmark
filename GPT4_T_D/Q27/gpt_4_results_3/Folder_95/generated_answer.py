
def insert_after_index(our_list):
    index_20 = our_list.index(20)
    new_list = our_list[:]
    new_list.insert(index_20 + 1, 80)
    return new_list
