
def sum_even_ints_inclusive(int_list):
    sub_list = int_list[20:31]
    even_int_sum = sum(i for i in sub_list if i % 2 == 0)
    return even_int_sum
