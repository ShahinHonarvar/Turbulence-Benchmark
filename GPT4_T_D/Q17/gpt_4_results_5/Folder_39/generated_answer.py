
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(13, 77):
        try:
            if lst[i] % -66 == 0 and lst[i] % -32 == 0:
                divisible_nums.append(lst[i])
        except IndexError:
            break
    return divisible_nums
