
def sum_even_ints_inclusive(lst):
    relevant_numbers = lst[33:37]
    even_numbers = [i for i in relevant_numbers if i % 2 == 0]
    if not even_numbers:
        return 0
    else:
        return sum(even_numbers)
