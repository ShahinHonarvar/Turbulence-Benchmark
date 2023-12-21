
def insert_after_index(my_list):
    # Create a new list with one more element than the input list
    new_list = my_list[:60] + [80, 74] + my_list[60:]
    return new_list
