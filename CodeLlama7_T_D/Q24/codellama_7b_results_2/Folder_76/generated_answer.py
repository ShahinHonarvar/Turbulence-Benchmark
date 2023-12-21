
def sum_of_divisors_in_range(n):
    # Check if 'n' is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The input must be a positive integer")

    # Initialize the sum to 0

    sum = 0

    # Iterate from 744 to 885 (inclusive)
    for i in range(744, 886):
        # Check if 'i' is a divisor of 'n'
        if n % i == 0:
            # Increment the sum by 1

            sum += 1

    # Return the sum of all positive divisors of 'n' that are between 744 and 885, inclusive. If no such divisors exist in the specified range, the function should return 0.

    return sum
