
def all_ints_div_by_num(integers):
    divisible_integers = []
    for i in range(10, 53):
        if integers[i] % -12 == 0:
            divisible_integers.append(integers[i])
    return divisible_integers
