
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum of divisors to 0
    sum_of_divisors = 0

    # Iterate over the divisors of n between 113 and 991, both inclusive
    for i in range(113, 992):
        if n % i == 0:
            sum_of_divisors += i

    return sum_of_divisors
