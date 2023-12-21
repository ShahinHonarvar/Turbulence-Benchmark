
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 1 to n
    for i in range(1, n + 1):

        # Check if i is a divisor of n
        if n % i == 0:

            # If i is a divisor of n, check if it is between 11 and 41
            if 11 <= i <= 41:

                # If i is between 11 and 41, add it to the list of divisors
                divisors.append(i)

    # Return the list of divisors in the specified range
    return divisors
