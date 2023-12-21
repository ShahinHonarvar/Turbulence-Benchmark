
def all_ints_div_by_num(lst):
    divisible_nums = []
    for i in range(6):
        if lst[i] % 6 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
