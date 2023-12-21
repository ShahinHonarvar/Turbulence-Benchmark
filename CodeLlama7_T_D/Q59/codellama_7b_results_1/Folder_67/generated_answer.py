
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Iterate over the tuple of positive integers
    for num in tuple:

        # Check if the number is a prime number
        if is_prime(num):

            # If the number is prime, check if it is left-truncatable prime
            if is_left_truncatable_prime(num):

                # If the number is both prime and left-truncatable prime, add it to the list
                prime_list.append(num)

    # Sort the list in descending order
    prime_list.sort(reverse=True)

    # Return the list of all left-truncatable prime numbers less than x
    return prime_list

# Function to check if a number is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Check if n is divisible by any number between 2 and n-1
        for i in range(2, n):
            if n % i == 0:
                return False

        # If no number between 2 and n-1 divides n, it is prime
        return True

# Function to check if a number is left-truncatable prime
def is_left_truncatable_prime(n):

    # Check if n is prime
    if not is_prime(n):
        return False

    # Iterate over the digits of n in reverse order
    for digit in str(n)[::-1]:

        # Remove the leading leftmost digit from n
        n = int(str(n)[:-1])

        # Check if the resulting number is prime
        if not is_prime(n):
            return False

    # If all checks pass, it is a left-truncatable prime number
    return True
