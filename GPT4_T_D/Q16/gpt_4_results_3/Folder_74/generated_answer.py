
def sum_even_ints_inclusive(int_list):
    return sum(num for ind, num in enumerate(int_list[17:79]) if num % 2 == 0)
