
def sum_even_ints_inclusive(integers):
    return sum(integers[111:112]) if any(num % 2 == 0 for num in integers[111:112]) else 0
