
def sum_odd_ints_inclusive(int_list):
    valid_range = int_list[30:88]
    sum_odd = sum(i for i in valid_range if i % 2 != 0)
    return sum_odd
