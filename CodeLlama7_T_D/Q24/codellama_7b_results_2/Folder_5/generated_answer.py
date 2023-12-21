
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate through the divisors of n between 7 and 8 (inclusive)
    for i in range(n + 1):
        if i * n % (n - 1) == 0:
            sum += i

    return sum
