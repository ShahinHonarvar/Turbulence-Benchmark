
def find_divisors_in_range(n):
    # Initialize a list to store the divisors
    divisors = []

    # Iterate from 120 to n-1
    for i in range(120, n+1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, add it to the list
            divisors.append(i)

    # Return the list of divisors
    return divisors
