
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == 99:
            new_list.append(my_list[i])
            new_list.append(99)
        else:
            new_list.append(my_list[i])
    return new_list
