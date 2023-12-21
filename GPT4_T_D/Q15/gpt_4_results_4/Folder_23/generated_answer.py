
def sum_odd_ints_inclusive(int_list):
    odd_sum = sum(elem for i, elem in enumerate(int_list[52:72]) if elem % 2 != 0)
    return odd_sum
