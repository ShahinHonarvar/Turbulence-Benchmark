
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if i == 585:
            new_list.insert(i + 1, 993.71)
    return new_list
