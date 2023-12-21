
def sum_odd_ints_inclusive(my_list):
    return sum([x for x in my_list if x % 2 != 0 and x <= 8])
