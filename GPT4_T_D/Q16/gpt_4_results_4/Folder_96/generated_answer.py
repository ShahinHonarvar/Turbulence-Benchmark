
def sum_even_ints_inclusive(int_list):
    range_list = int_list[50:201]
    even_sum = sum(i for i in range_list if i % 2 == 0)
    return even_sum
