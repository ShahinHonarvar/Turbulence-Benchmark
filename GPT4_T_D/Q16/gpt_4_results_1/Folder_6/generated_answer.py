
def sum_even_ints_inclusive(int_list):
    return sum(num for index, num in enumerate(int_list[10:67]) if num % 2 == 0)
