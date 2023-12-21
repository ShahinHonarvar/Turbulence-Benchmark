
def insert_after_index(my_list):
    index = my_list.index(30) + 1
    new_list = my_list[:index] + [37] + my_list[index:]
    return new_list
