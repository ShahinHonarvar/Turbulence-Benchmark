
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if i == 15:
            new_list.insert(i+1, 550.97)
    return new_list
