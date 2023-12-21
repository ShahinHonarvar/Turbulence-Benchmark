
def sum_even_ints_inclusive(int_list):
    even_integers_sum = sum(val for idx, val in enumerate(int_list) if 15 <= idx <= 39 and val % 2 == 0)
    return even_integers_sum
