
def all_ints_div_by_num(int_list):
    divisible_ints = []
    for i in range(10, 57):
        if i < len(int_list):
            if int_list[i] % 16 == 0:
                divisible_ints.append(int_list[i])
    return divisible_ints
