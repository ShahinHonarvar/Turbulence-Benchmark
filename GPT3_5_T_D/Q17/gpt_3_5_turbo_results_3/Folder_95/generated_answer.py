
def all_ints_div_by_both_two_nums(integers):
    divisible_ints = []
    for i in range(57, 85):
        if integers[i] % -30 == 0 and integers[i] % -88 == 0:
            divisible_ints.append(integers[i])
    return divisible_ints
