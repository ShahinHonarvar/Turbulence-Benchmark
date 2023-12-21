
def all_ints_div_by_num(integers):
    divisible_integers = []
    for i in range(574, 745):
        if integers[i] % 649 == 0:
            divisible_integers.append(integers[i])
    return divisible_integers
