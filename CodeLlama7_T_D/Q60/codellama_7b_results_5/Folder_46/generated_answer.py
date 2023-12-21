
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than or equal to x
    for i in range(1, x+1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number can be obtained by successively removing leading and trailing digits
            if is_left_right_truncatable_prime(i):

                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Return the list of prime numbers in sorted order
    return sorted(prime_numbers)

# Define a function to check if a number is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n**0.5)+1):

            # If any factor divides n, return False
            if n % i == 0:
                return False

    # If no factors are found, return True
    return True

# Define a function to check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n**0.5)+1):

            # If any factor divides n, return False
            if n % i == 0:
                return False

    # Check if the number can be obtained by successively removing leading and trailing digits
    if str(n)[:-2] == str(n)[2:] or str(n)[:-1] == str(n)[1:] or str(n)[:-3] == str(n)[3:]:
        # If the number can be obtained by successively removing leading and trailing digits, return True
        return True

    # If no factors are found and the number cannot be obtained by successively removing leading and trailing digits, return False
    return False
