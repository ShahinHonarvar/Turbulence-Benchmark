
def insert_after_index(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            new_list.append(my_list[i])
        else:
            new_list.append(my_list[i])
            if my_list[i+1] == 99:
                new_list.append(99)
    return new_list
