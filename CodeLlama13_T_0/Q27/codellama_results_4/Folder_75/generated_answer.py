
def insert_after_index(my_list):
    index = my_list.index(99) + 1
    return my_list[:index] + [99] + my_list[index:]
