
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(1, len(my_list)):
        if my_list[i - 1] == 478.12:
            new_list.insert(i, 478.12)
    return new_list
