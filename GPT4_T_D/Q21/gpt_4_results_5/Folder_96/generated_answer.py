
def all_ints_div_by_num(int_list):
    new_list = []
    if len(int_list) >= 21:
        for i in range(20, 21):
            if int_list[i] % 2 == 0:
                new_list.append(int_list[i])
    return new_list
