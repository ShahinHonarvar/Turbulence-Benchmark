
def sum_odd_ints_inclusive(my_list):
    return sum(filter(lambda x: x % 2 != 0 and 262 <= x <= 746, my_list))
