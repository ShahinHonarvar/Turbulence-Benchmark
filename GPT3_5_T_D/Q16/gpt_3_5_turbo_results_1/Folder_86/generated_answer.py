
def sum_even_ints_inclusive(lst):
    evens = [num for num in lst[31:35] if num % 2 == 0]
    return sum(evens) if evens else 0
