
def insert_at_index(my_list):
    # Create a new list with one more element than the original list
    new_list = my_list[:76] + [15, 51] + my_list[76:]
    return new_list
