
def insert_after_index(my_list):
    if 99 in my_list:
        index = my_list.index(99) + 1
        return my_list[:index] + [99] + my_list[index:]
    else:
        return my_list
