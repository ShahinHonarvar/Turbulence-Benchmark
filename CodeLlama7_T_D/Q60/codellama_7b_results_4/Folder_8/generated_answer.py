
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through the range of integers from 1 to x
    for i in range(1, x + 1):

        # Check if the current integer is a prime number
        if is_prime(i):

            # If the current integer is a prime number, check if it is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # If the current integer is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_list.append(i)

    # Sort the list of prime numbers in descending order
    prime_list.sort(reverse=True)

    # Return the list of prime numbers
    return prime_list

# Define a function to check if an integer is a prime number
def is_prime(n):

    # Check if n is an integer greater than 1
    if type(n) != int or n <= 1:
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If no prime factor was found, return True
    return True

# Define a function to check if an integer is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)) - 1, 0, -1):
        num = int(str(n)[:i] + str(n)[i+1:]))
        if not is_prime(num):
            return False

    # If no prime factor was found, return True
    return True
