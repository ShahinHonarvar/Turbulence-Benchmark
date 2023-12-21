
def sum_even_ints_inclusive(int_list):
    return sum(num for num in int_list[:9] if num % 2 == 0)
