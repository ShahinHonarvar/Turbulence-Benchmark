
def sum_even_ints_inclusive(integer_list):
    even_ints = [i for i in integer_list[29:30] if i % 2 == 0]
    return sum(even_ints) if even_ints else 0
