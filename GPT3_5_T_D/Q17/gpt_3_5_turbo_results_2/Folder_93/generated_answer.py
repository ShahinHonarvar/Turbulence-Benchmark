
def all_ints_div_by_both_two_nums(integers):
    divisible_ints = []
    for i in range(86, 90):
        if integers[i] % -61 == 0 and integers[i] % -79 == 0:
            divisible_ints.append(integers[i])
    return divisible_ints
