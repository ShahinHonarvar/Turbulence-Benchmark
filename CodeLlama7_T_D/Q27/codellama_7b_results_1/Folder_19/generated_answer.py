
def insert_after_index(my_list):
    # Insert 0.78 at index immediately succeeding index 49
    new_list = my_list[:50] + [0.78] + my_list[50:]
    return new_list
