
def all_ints_div_by_num(integers):
    divisible_ints = []
    for i in range(14, 69):
        if i < len(integers) and integers[i] % 18 == 0:
            divisible_ints.append(integers[i])
    return divisible_ints
