
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i == 74:
            new_list.extend(my_list[i:])
            new_list.insert(i + 1, 49)
            return new_list
    else:
        new_list = my_list[:]
        new_list.append(49)
        return new_list
