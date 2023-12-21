
def sum_even_ints_inclusive(int_list):
    relevant_numbers = int_list[12:93]
    sum_evens = sum(num for num in relevant_numbers if num % 2 == 0)
    return sum_evens
