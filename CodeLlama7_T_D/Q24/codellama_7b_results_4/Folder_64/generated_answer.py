
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate through the divisors of n between 1 and 9 (inclusive)
    for i in range(1, 10):
        if n % i == 0:
            sum += i

    # Return the sum of all positive divisors of n that are between 1 and 9 (inclusive), or 0 if no such divisors exist
    return sum
