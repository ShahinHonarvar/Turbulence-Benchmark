
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate through the divisors of n between 32 and 35, both inclusive
    for i in range(32, 36):
        if n % i == 0:
            sum += i

    return sum
