
def insert_after_index(my_list):
    # Find the index of the element after which we want to insert [312, 441]
    index = my_list.index(427) + 1
    # Insert [312, 441] at the found index in the original list
    new_list = my_list[:index] + [312, 441] + my_list[index:]
    return new_list
