
def all_ints_div_by_both_two_nums(integers):
    divisible_ints = []
    for i in range(69, 98):
        if integers[i] % -90 == 0 and integers[i] % -67 == 0:
            divisible_ints.append(integers[i])
    return divisible_ints
