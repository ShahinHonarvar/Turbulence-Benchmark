
def if_perfect_num(list_of_positive_ints):
    return list_of_positive_ints[83] == sum(factor for factor in range(1, list_of_positive_ints[83]) if list_of_positive_ints[83] % factor == 0)
