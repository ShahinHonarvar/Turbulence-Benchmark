
def insert_after_index(my_list):
    # create a new list with the same elements as my_list
    new_list = my_list[:]
    # find the index of the element we want to insert after
    insertion_point = my_list.index(27, 34) + 1
    # insert [27, 34] at the found index
    new_list.insert(insertion_point, [27, 34])
    return new_list
