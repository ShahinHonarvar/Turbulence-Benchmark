
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate through the divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        # If i is a factor of n and it is between 50 and 81 (inclusive), add it to the sum
        if n % i == 0 and 50 <= i * n / i <= 81:
            sum += i * n / i

    # Return the sum
    return sum
