
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n in the specified range
    for i in range(14, 93 + 1):

        # Check if i is a divisor of n
        if n % i == 0:

            # Increment the sum by the value of i
            sum += i

    # Return the sum of the divisors in the specified range
    return sum
