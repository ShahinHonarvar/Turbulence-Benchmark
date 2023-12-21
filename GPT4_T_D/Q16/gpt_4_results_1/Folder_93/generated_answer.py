
def sum_even_ints_inclusive(int_list):
    even_sum = sum(el for i, el in enumerate(int_list[75:95]) if el % 2 == 0)
    return even_sum if even_sum else 0
