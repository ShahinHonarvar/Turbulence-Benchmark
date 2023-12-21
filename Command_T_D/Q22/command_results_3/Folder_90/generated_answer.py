def find_sum_of_multiples(n):
    # Instead of using a for loop, we will use the range() function
    # with a list comprehension. This will be much faster!
    return n * (n + 1) * (2 * n + 1) / 6
