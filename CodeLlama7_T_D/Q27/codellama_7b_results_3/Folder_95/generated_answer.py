
def insert_after_index(my_list):
    # Create a new list with an extra element
    new_list = my_list[:20] + [80] + my_list[20:]
    return new_list
