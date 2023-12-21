
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate through the divisors of n
    for i in range(1, n + 1):

        # Check if i is a divisor of n
        if n % i == 0:

            # Check if i is between 15 and 20 (inclusive)
            if 15 <= i <= 20:
                sum += i

    # Return the sum of all positive divisors of n that are between 15 and 20 (inclusive)
    return sum
