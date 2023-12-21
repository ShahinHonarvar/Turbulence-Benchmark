
def sum_even_ints_inclusive(int_list):
    if len(int_list) > 111:
        range_list = int_list[111:112]
        total_sum = sum(i for i in range_list if i % 2 == 0)
        return total_sum
    else:
        return 0
