
def insert_at_index(my_list):
    # Create a new list with an extra element at index 85
    new_list = my_list[:85] + [41, 95] + my_list[85:]
    return new_list
