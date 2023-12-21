
def sum_of_divisors_in_range(n):
    # Initialize sum variable
    div_sum = 0

    # Loop through numbers from 228 to 846 (both inclusive)
    for i in range(228, 847):
        # Check if current number is a divisor of n
        if n % i == 0:
            # Add the divisor to the sum
            div_sum += i

    # Return the sum of divisors in the range or 0 if none exist
    return div_sum
