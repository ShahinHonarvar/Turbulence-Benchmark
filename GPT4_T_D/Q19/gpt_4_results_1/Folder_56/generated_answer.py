
def all_ints_not_div_by_num(my_list):
    new_list = []
    for index in range(8, 9):
        if my_list[index] % -9 != 0:
            new_list.append(my_list[index])
    return new_list
