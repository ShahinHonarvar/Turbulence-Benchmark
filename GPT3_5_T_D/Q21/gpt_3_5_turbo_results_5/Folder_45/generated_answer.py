
def all_ints_div_by_num(int_list):
    divisible_list = []
    for i in range(len(int_list)):
        if i >= 0 and i <= 2 and int_list[i] % 9 == 0:
            divisible_list.append(int_list[i])
    return divisible_list
