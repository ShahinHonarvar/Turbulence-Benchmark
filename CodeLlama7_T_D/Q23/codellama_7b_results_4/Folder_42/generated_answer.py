
def find_divisors_in_range(n):
    # Create a list of all divisors in the range
    divisors = []

    # Iterate from 14 to n-1
    for i in range(14, n+1):
        # If i is a divisor of n, add it to the list
        if n % i == 0:
            divisors.append(i)

    # Return the list of divisors in the specified range
    return divisors
