
def insert_after_index(my_list):
    # Find the index of the first occurrence of 29
    idx = my_list.index(29)
    # Insert [28, 53] at the next index
    new_list = my_list[:idx + 1] + [28, 53] + my_list[idx + 1:]
    return new_list
