
def all_ints_not_div_by_num(int_list):
    new_list = []
    for index in range(46, 72):
        if index < len(int_list):
            if int_list[index] % 93 != 0:
                new_list.append(int_list[index])
    return new_list
