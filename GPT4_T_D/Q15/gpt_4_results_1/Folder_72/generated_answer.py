
def sum_odd_ints_inclusive(integers):
    return sum(num for idx, num in enumerate(integers[29:52]) if num % 2 != 0)
