
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 7 to n-1, checking if each number is a divisor of n
    for i in range(7, n+1):
        if n % i == 0:
            # If it is a divisor, add it to the list
            divisors.append(i)

    # Return the list of divisors
    return divisors
