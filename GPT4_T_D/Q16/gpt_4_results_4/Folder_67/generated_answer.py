
def sum_even_ints_inclusive(integer_list):
    sum_even = sum([num for num in integer_list[22:51] if num % 2 == 0])
    return sum_even if sum_even != 0 else 0
