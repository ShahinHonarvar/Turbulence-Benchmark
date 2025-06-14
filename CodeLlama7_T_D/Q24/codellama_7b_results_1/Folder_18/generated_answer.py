
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate through the divisors of n between 387 and 516 (both inclusive)
    for i in range(387, 517):
        if n % i == 0:
            sum += i

    # Return the sum of all positive divisors of n that are between 387 and 516, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    return sum
