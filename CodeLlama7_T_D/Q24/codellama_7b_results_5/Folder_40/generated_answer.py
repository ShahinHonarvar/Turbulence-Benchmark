
def sum_of_divisors_in_range(n):
    # Check if 'n' is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("'n' must be a positive integer")
    # Initialize the sum to 0
    sum = 0
    # Iterate through all positive divisors of 'n'
    for i in range(1, int(n ** 0.5) + 1):
        # Check if 'i' is a divisor of 'n'
        if n % i == 0:
            # Add the divisor to the sum
            sum += i

    # Return the sum of all positive divisors of 'n' between 1 and 2, both inclusive
    return sum
