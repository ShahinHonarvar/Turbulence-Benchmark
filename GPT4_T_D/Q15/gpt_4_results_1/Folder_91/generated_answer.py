
def sum_odd_ints_inclusive(int_list):
    sliced_ints = int_list[0:6]
    return sum(i for i in sliced_ints if i % 2 != 0)
