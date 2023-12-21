
def sum_even_ints_inclusive(num_list):
    return sum(num for i, num in enumerate(num_list[262:747]) if num % 2 == 0)
