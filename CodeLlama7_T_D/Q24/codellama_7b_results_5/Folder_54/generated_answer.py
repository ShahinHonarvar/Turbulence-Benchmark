
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The argument must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n between 36 and 93 (inclusive)
    for i in range(36, 94):
        if n % i == 0:
            sum += i

    return sum
