
def insert_after_index(my_list):
    # Find the index of the first occurrence of 70 in the list
    start_index = my_list.index(70)
    # Insert 76 at the next index after start_index
    new_list = my_list[:start_index + 1] + [76] + my_list[start_index + 1:]
    return new_list
