
def all_ints_div_by_num(integers):
    divisible_nums = []
    for i in range(52, 54):
        if integers[i] % 93 == 0:
            divisible_nums.append(integers[i])
    return divisible_nums
