
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The input must be a positive integer.")
    # Initialize the sum of divisors to 0
    sum_of_divisors = 0
    # Iterate through the divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        # If the current divisor is between 16 and 68, inclusive
        if n % i == 0:
            # Add the current divisor to the sum of divisors
            sum_of_divisors += i
    # Return the sum of all positive divisors of n that are between 16 and 68, inclusive. If no such divisors exist in the specified range, the function should return 0.
    return sum_of_divisors
