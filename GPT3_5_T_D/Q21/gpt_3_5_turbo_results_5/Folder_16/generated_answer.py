
def all_ints_div_by_num(integers):
    divisible_integers = []
    for i in range(13, 69):
        if integers[i] % 71 == 0:
            divisible_integers.append(integers[i])
    return divisible_integers
