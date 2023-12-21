
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is a divisor, check if it is between 35 and 55
            if 35 <= i <= 55:
                # If it is between 35 and 55, add it to the list of divisors
                divisors.append(i)

    # Return the list of divisors in the specified range
    return divisors
