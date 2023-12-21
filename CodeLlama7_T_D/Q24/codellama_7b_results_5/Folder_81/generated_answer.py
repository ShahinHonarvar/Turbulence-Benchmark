
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n
    for i in range(1, n + 1):

        # Check if i is a divisor of n
        if n % i == 0:

            # Increment the sum by i if it is between 3 and 4, both inclusive
            if 3 <= i <= 4:
                sum += i

    # Return the sum
    return sum
