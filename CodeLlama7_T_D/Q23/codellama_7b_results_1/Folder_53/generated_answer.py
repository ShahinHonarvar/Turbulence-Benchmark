
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all positive integers between 4 and 9 (both inclusive)
    for i in range(4, 10):

        # If 'i' is a divisor of 'n', add it to the list
        if n % i == 0:
            divisors.append(i)

    # Return the list of all positive divisors of 'n' that are between 4 and 9 (both inclusive), or an empty list if no such divisors exist
    return divisors
