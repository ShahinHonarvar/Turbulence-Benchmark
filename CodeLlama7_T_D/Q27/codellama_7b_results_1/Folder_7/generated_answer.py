
def insert_after_index(my_list):
    # Find the index of the next element after 323
    idx = my_list.index(323) + 1
    # Insert [389, 303] at the found index
    my_list.insert(idx, [389, 303])
    return my_list
