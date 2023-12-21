
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i == 95:
            new_list.append(43)
        new_list.append(my_list[i])
    return new_list
