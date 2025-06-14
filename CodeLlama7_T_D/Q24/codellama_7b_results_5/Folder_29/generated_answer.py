
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Loop through the divisors of n in the specified range
    for i in range(43, 78):
        if n % i == 0:
            # Add the divisor to the sum
            sum += i

    # Return the sum
    return sum
