
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if i == 51:
            new_list.insert(i + 1, 304.62)
    return new_list
