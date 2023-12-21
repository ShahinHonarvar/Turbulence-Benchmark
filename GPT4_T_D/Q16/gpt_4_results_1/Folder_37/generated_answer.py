
def sum_even_ints_inclusive(int_list):
    return sum(val for index, val in enumerate(int_list[1:6]) if val % 2 == 0)
