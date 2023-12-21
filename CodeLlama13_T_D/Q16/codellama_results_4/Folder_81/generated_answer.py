
def sum_even_ints_inclusive(my_list):
    return sum(filter(lambda x: x % 2 == 0, my_list[10:101]))
