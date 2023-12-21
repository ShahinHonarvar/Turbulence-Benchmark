
def insert_at_index(my_list):
    # Create a new list with an extra element
    new_list = my_list[:55] + [26, 10] + my_list[55:]
    return new_list
