
def insert_at_index(my_list):
    # Insert [28, 53] at index 29
    new_list = my_list[:29] + [28, 53] + my_list[29:]
    return new_list
