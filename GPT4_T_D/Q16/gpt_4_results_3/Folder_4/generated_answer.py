
def sum_even_ints_inclusive(my_list):
    return sum(value for index, value in enumerate(my_list[12:93]) if value % 2 == 0)
