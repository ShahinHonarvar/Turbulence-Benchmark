
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == 42:
            new_list.insert(i+1, 53)
    return new_list
