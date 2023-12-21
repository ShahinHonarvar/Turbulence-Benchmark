
def sum_even_ints_inclusive(input_list):
    even_sum = sum(i for i in input_list[10:67] if i % 2 == 0)
    return even_sum if even_sum > 0 else 0
