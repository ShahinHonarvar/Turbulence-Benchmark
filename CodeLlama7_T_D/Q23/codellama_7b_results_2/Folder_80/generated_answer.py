 def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all integers between 70 and 93, inclusive
    for i in range(70, 94):

        # If 'i' is a divisor of 'n', add it to the list
        if n % i == 0:
            divisors.append(i)

    # Return the list of all positive divisors of 'n' that are between 70 and 93, inclusive
    return divisors
