
def insert_at_index(my_list):
    # Insert [40, 27] at index 44
    new_list = my_list[:44] + [40, 27] + my_list[44:]
    return new_list
