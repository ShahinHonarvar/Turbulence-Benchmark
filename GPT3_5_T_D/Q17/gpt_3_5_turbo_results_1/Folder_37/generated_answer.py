
def all_ints_div_by_both_two_nums(integers):
    divisible_integers = []
    for i in range(2, 8):
        if integers[i] % -1 == 0 and integers[i] % -7 == 0:
            divisible_integers.append(integers[i])
    return divisible_integers
