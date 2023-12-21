
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i == 57:
            new_list.extend([my_list[i], 76])
        else:
            new_list.append(my_list[i])
    return new_list
