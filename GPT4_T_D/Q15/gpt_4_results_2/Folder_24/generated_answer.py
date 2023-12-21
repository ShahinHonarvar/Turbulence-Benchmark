
def sum_odd_ints_inclusive(int_list):
    sliced_list = int_list[74:96]
    return sum(i for i in sliced_list if i % 2 != 0)
