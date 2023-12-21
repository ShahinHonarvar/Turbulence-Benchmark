
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
            # Increment the sum by i
            sum += i

            # If i is greater than 4, also increment the sum by n / i
            if i > 4:
                sum += n // i

    # Return the sum of all positive divisors of n that are between 4 and 5, both inclusive
    return sum
