
def insert_after_index(my_list):
    index = my_list.index(94) + 1
    return my_list[:index] + [93] + my_list[index:]
