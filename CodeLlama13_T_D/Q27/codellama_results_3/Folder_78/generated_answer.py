
def insert_after_index(my_list):
    index = 63
    new_list = my_list[:index + 1] + [99] + my_list[index + 1:]
    return new_list
