
def insert_at_index(my_list):
    # Insert 15 at index 99
    new_list = my_list[:99] + [15] + my_list[99:]
    return new_list
