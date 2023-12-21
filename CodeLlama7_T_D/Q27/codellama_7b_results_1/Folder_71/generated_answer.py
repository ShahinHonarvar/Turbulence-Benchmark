
def insert_after_index(my_list):
    # Find the index of 70 in the list
    index_of_70 = my_list.index(70)
    # Insert 76 at the index immediately succeeding index 70
    new_list = my_list[:index_of_70 + 1] + [76] + my_list[index_of_70 + 1:]
    return new_list
