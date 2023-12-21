
def sum_even_ints_inclusive(int_list):
    even_ints = [i for i in int_list[82:87] if i % 2 == 0]
    return sum(even_ints) if even_ints else 0
