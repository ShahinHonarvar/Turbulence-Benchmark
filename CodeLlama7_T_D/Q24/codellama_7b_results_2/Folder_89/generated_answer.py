
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Increment the sum by the divisor
            sum += i

            # If the divisor is greater than 14 and less than or equal to 48, include it in the sum
            if i > 14 and i <= 48:
                sum += n // i

    # Return the sum of all positive divisors of n that are between 14 and 48, both inclusive
    return sum
