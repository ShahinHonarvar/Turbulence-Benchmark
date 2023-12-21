
def all_ints_not_div_by_num(num_list):
    new_list = []
    for i in range(1, min(7, len(num_list))):
        if num_list[i] % 7 != 0:
            new_list.append(num_list[i])
    return new_list
