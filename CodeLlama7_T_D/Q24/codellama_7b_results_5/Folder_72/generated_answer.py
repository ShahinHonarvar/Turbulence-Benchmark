
def sum_of_divisors_in_range(n):
    # Check if 'n' is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("'n' must be a positive integer")
    # Initialize the sum to 0
    sum = 0
    # Iterate from 32 to 90 (both inclusive)
    for i in range(32, 91):
        # Check if 'i' divides 'n' evenly
        if n % i == 0:
            # Add 'i' to the sum
            sum += i

    # Return the sum of all positive divisors of 'n' in the specified range (32 to 90, both inclusive) or 0 if no such divisors exist.
    return sum
