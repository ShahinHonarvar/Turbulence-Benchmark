def find_sum_of_multiples(n):
    # List of first 257 positive multiples of the given integer
    x = []
    # Add the given integer to the list of multiples
    for i in range(1, 257):
        x.append(n + i)
    # Sum of all the multiples
    return sum(x)
