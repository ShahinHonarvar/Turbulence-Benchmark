
def all_ints_div_by_num(integers):
    divisible_integers = []
    for i in range(43, 60):
        if integers[i] % 22 == 0:
            divisible_integers.append(integers[i])
    return divisible_integers
