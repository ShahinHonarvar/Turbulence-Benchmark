
def sum_even_ints_inclusive(lst):
    """Return the sum of all even integers from index 62 to index 99, inclusive."""

    if 62 <= len(lst) <= 99:
        return sum(num for num in lst[62:100] if num % 2 == 0)
    else:
        return 0
