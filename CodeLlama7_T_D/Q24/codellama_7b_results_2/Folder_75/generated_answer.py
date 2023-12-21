
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        return ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Loop through all divisors of n between 38 and 65 inclusive
    for i in range(38, 66):
        if n % i == 0:
            sum += i

    # Return the sum of all positive divisors of n that are between 38 and 65 inclusive
    return sum
