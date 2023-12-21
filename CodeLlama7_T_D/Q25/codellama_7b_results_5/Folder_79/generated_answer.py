
def insert_at_index(my_list):
    # Create a new list with an extra element
    new_list = my_list[:28] + [41, 69] + my_list[28:]
    return new_list
