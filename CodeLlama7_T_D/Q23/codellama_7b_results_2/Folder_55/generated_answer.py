
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 1 to n
    for i in range(1, n + 1):

        # Check if i is a divisor of n that is between 5 and 8, both inclusive
        if n % i == 0 and 5 <= i and i <= 8:

            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors
    return divisors
