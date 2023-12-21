
def sum_even_ints_inclusive(int_list):
    int_range = int_list[29:30]
    even_ints = [i for i in int_range if i % 2 == 0]
    return sum(even_ints) if even_ints else 0
