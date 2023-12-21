
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

            # Check if i is between 50 and 84 (inclusive)
            if 50 <= i <= 84:
                sum += i

    # Return the sum of the divisors in the specified range
    return sum
