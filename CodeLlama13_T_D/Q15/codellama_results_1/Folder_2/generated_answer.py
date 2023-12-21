
def sum_odd_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list[15:40]) if i % 2 == 1)
