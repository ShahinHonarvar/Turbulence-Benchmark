
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the current number is a prime number
        if is_prime(i):

            # If the current number is a prime number, check if it is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # If the current number is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # If i divides n, return False
                return False

    # If n is greater than 1 and does not have any factors other than 1 and itself, return True
    return True

def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        # If n is not a prime number, return False
        return False

    # Loop through all numbers from 1 to the length of the string representation of n
    for i in range(1, len(str(n))) + 1:

        # Check if removing the leading leftmost and last rightmost digits of n simultaneously successively results in a prime number
        if is_prime(int(str(n)[i:] + str(n)[:i]))) :

            # If removing the leading leftmost and last rightmost digits of n simultaneously successively results in a prime number, return True
            return True

    # If no left-and-right-truncatable prime number exists in the specified range, return False
    return False
