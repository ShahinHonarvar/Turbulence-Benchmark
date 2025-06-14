
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the tuple of integers
    for x in tuple:

        # Check if the integer is a prime number
        if is_prime(x):

            # Initialize a variable to store the leading digit of the integer
            leading_digit = 0

            # Continue removing the leftmost digit from the integer until it becomes 1 or less
            while x > 1:

                # Check if the remaining number is a prime number
                if is_prime(x):

                    # Add the prime number to the result list
                    result.append(x)

                # Remove the leftmost digit from the integer
                x = int(str(x)[1:]))

        # Check if the integer is equal to 1 or less
        if x <= 1:

            # Add the prime number to the result list
            result.append(x)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(result, reverse=True)

# Check if an integer is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Initialize a variable to store the result of the primality test
        prime = True

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Set prime to False
                prime = False

                # Break the loop
                break

        # Return the result of the primality test
        return prime
