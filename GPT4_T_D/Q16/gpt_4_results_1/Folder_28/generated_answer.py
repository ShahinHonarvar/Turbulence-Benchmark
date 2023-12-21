
def sum_even_ints_inclusive(int_list):
    subset = int_list[62:64]
    even_sum = sum(num for num in subset if num % 2 == 0)
    return even_sum
