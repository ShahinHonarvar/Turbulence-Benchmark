
def sum_odd_ints_inclusive(int_list):
    subset_list = int_list[60:201]
    sum_odd = sum(i for i in subset_list if i % 2 != 0)
    return sum_odd
