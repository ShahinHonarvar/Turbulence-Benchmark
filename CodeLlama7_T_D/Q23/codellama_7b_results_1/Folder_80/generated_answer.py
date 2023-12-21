
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 1 to n-1
    for i in range(1, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor of n, check if it is between 70 and 93
            if 70 <= i <= 93:
                # If i is between 70 and 93, add it to the list of divisors
                divisors.append(i)

    # Return the list of divisors that are between 70 and 93
    return divisors
