
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == 412:
            new_list.insert(i+1, 668)
    return new_list
