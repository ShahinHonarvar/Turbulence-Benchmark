
def sum_of_divisors_in_range(n):
    # Check if 'n' is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("'n' must be a positive integer")
    # Initialize the sum to 0
    sum = 0
    # Loop through all divisors of 'n' between 2 and 6 (both inclusive)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i

    return sum
