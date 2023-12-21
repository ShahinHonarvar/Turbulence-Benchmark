
def insert_at_index(my_list):
    # Create a new list with an extra element at index 427
    new_list = my_list[:427] + [312, 441] + my_list[427:]
    return new_list
