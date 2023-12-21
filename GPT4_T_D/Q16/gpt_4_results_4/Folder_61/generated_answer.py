
def sum_even_ints_inclusive(num_list):
    return sum(num for num in num_list[:8] if num % 2 == 0)
