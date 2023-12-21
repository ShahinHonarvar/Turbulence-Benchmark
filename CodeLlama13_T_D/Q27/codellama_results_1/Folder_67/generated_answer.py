
def insert_after_index(my_list):
    index = my_list.index(44) + 1
    new_list = list(my_list[:index])
    new_list.append(76)
    new_list.extend(my_list[index:])
    return new_list
