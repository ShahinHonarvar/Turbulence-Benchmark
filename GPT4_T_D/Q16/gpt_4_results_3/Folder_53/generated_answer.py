
def sum_even_ints_inclusive(int_list):
    slice_list = int_list[111:112]
    return sum(i for i in slice_list if i % 2 == 0)
