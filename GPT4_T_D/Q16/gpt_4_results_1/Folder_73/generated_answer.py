
def sum_even_ints_inclusive(int_list):
    sliced_list = int_list[19:93]
    even_sum = sum(num for num in sliced_list if num % 2 == 0)
    return even_sum
