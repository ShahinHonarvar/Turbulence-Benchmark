
def insert_at_index(my_list):
    # create a new list with the original elements plus the new element at index 30
    new_list = my_list[:30] + [37] + my_list[30:]
    return new_list
