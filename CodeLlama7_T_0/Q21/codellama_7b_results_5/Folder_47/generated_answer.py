
def all_ints_div_by_num(my_list):
    divisible_ints = []
    for i in range(75, 89):
        if my_list[i] % -27 == 0:
            divisible_ints.append(my_list[i])
    return divisible_ints
