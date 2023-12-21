
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if i == 76:
            new_list.insert(i+1, 10.01)
    return new_list
