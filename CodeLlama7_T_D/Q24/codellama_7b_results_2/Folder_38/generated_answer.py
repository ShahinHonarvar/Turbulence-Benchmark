
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n between 16 and 68 (inclusive)
    for i in range(16, 69):
        if n % i == 0:
            sum += i

    # Return the sum of the divisors in the specified range
    return sum
