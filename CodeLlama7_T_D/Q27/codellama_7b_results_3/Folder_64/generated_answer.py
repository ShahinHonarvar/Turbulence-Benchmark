
def insert_after_index(my_list):
    new_list = my_list[:]
    # find the index of 8 in the list
    index_of_eight = new_list.index(8)
    # insert [3, 8] at the next index after 8
    new_list.insert(index_of_eight + 1, [3, 8])
    return new_list
