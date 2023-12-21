
def insert_after_index(my_list):
    # Find the index of 43 in the list
    index_43 = my_list.index(43)
    # Insert 37 at the next index after 43
    new_list = my_list[:index_43 + 1] + [37] + my_list[index_43 + 1:]
    return new_list
