
def insert_after_index(my_list):
    index = 44
    new_value = 76
    return my_list[:index + 1] + [new_value] + my_list[index + 1:]
