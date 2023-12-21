
def sum_even_ints_inclusive(lst):
    return sum(num for idx, num in enumerate(lst) if idx >= 21 and idx <= 97 and num % 2 == 0)
