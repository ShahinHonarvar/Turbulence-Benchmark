
def sum_even_ints_inclusive(my_list):
    return sum([num for i, num in enumerate(my_list) if i >= 6 and num % 2 == 0])
