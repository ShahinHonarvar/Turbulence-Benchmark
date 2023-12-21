
def insert_after_index(my_list):
    index = 43
    new_list = my_list[:index+1] + [37] + my_list[index+1:]
    return new_list
