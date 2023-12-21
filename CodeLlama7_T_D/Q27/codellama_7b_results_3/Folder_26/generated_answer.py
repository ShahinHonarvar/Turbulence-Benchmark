
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if i == 55:
            new_list.insert(i+1, [26, 10])
    return new_list
