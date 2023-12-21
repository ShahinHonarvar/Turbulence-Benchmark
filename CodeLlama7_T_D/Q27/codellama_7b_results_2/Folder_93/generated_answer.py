
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if i == 36:
            new_list.insert(i + 1, [54, 13])
    return new_list
