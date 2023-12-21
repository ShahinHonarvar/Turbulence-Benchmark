
def all_ints_div_by_num(lst):
    divisible_nums = []
    for i in range(66, 82):
        if lst[i] % 77 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
