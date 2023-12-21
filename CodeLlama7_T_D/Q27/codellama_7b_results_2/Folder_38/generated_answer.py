
def insert_after_index(my_list):
    # Find the index of the first occurrence of 89 in the list
    index_of_89 = my_list.index(89)
    # Insert 86 at the next index after the index of 89
    new_list = my_list[:index_of_89 + 1] + [86] + my_list[index_of_89 + 1:]
    return new_list
