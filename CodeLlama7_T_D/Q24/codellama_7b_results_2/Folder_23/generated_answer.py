
def sum_of_divisors_in_range(n):
    # Check if 'n' is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("'n' must be a positive integer.")
    # Initialize the sum to 0
    sum = 0
    # Loop through all divisors of 'n' between 18 and 52 (both inclusive)
    for i in range(18, 53):
        if n % i == 0:
            sum += i

    # Return the sum of all positive divisors of 'n' that are between 18 and 52 (both inclusive), or 0 if no such divisors exist in the specified range.
    return sum
