
def insert_after_index(my_list):
    index = 41
    new_list = my_list[:index+1] + [74, 70] + my_list[index+1:]
    return new_list
