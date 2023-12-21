
def insert_at_index(my_list):
    # create a new list with an additional element
    new_list = my_list[:99] + [15] + my_list[99:]
    return new_list
