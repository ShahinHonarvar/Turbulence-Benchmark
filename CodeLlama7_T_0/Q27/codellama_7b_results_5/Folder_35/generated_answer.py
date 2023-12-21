
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if i == 100:
            new_list.insert(i + 1, [876, 203])
    return new_list
