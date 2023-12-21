
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Loop through all divisors of n between 42 and 77 (inclusive)
    for i in range(42, 78):
        if n % i == 0:
            sum += i

    # Return the sum of all positive divisors of n within the specified range
    return sum
