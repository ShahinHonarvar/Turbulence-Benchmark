
def insert_after_index(my_list, index):
    if index >= len(my_list) or index < 0:
        raise ValueError("Index out of bounds")

    new_list = my_list[:index+1] + [912, 170] + my_list[index+1:]

    return new_list
