
def sum_of_divisors_in_range(n):
    # Check if 'n' is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("'n' must be a positive integer")
    # Initialize the sum to 0
    sum = 0
    # Loop through all divisors of 'n' between 5 and 9 (inclusive)
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            # If the current divisor is between 5 and 9 (inclusive), add it to the sum
            if 5 <= i <= 9:
                sum += i
    # Return the sum of all positive divisors of 'n' that are between 5 and 9 (inclusive)
    return sum
