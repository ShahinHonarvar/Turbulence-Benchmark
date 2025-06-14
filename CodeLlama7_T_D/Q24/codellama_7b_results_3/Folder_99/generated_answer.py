
def sum_of_divisors_in_range(n):
    # Check that n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    # Initialize the sum to 0
    sum = 0
    # Loop through all divisors of n between 378 and 782
    for i in range(378, 783):
        if n % i == 0:
            # Add the divisor to the sum
            sum += i

    return sum
