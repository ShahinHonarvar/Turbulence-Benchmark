
def sum_odd_ints_inclusive(int_list):
    sub_list = int_list[74:96]
    sum_odd = sum(i for i in sub_list if i % 2 != 0)
    return sum_odd
