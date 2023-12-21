
def sum_even_ints_inclusive(my_list):
    even_ints = [x for x in my_list if x % 2 == 0]
    return sum(even_ints)
