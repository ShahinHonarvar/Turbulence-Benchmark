
def insert_at_index(my_list):
    # Insert [33, 78] at index 93
    new_list = my_list[:93] + [33, 78] + my_list[93:]
    return new_list
