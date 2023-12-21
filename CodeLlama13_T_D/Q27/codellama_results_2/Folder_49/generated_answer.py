
def insert_after_index(my_list):
    index = 38
    new_list = my_list[:index+1] + [27, 34] + my_list[index+1:]
    return new_list
