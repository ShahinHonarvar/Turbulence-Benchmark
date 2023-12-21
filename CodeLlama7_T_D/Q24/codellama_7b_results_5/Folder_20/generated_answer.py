
def sum_of_divisors_in_range(n):
    # Initialize sum to 0
    sum = 0
    # Iterate through divisors between 28 and 81 (inclusive)
    for i in range(28, 82):
        # Check if current number is a divisor of n
        if n % i == 0:
            # Add current divisor to sum
            sum += i

    return sum
