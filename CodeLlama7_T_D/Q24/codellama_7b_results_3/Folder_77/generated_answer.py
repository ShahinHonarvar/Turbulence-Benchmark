
def sum_of_divisors_in_range(n):
    # Check that n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    # Initialize the sum of divisors to 0
    sum_divisors = 0
    # Iterate over the divisors of n in the specified range
    for i in range(111, 508 + 1):
        if n % i == 0:
            # Add the divisor to the sum
            sum_divisors += i
    return sum_divisors
