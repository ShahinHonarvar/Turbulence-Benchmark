
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        # If i is a divisor of n and between 40 and 74 inclusive
        if n % i == 0 and 40 <= (i * 2 - 1) / 2 <= 74:
            # Add the divisor to the sum
            sum += i

    # Return the sum of all positive divisors of n between 40 and 74 inclusive, or 0 if no such divisors exist in the specified range
    return sum
