
def sum_even_ints_inclusive(input_list):
    sliced_list = input_list[60:201]
    sum_even = sum([x for x in sliced_list if x % 2 == 0])
    return sum_even
