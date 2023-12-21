
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate through the divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # Increment the sum by the absolute value of i
            sum += abs(i)

    # Return the sum of all positive divisors of n that are between 315 and 955, both inclusive
    return sum if 315 <= sum <= 955 else 0
