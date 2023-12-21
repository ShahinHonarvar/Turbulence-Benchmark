
def insert_at_index(my_list):
    # Create a new list with an extra element
    new_list = my_list[:598] + [385, 999] + my_list[598:]
    return new_list
