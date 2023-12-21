
def sum_even_ints_inclusive(integer_list):
    return sum(i for i in integer_list[:7] if i % 2 == 0)
