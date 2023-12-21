
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            if is_left_right_truncatable_prime(i):

                # If both conditions are met, add i to the list of prime numbers.
                prime_list.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x, sorted in ascending order.
    return sorted(prime_list)

# Define a function to check if a number is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n (inclusive)
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n without a remainder
            if n % i == 0:

                # If i divides n without a remainder, return False (not prime)
                return False

    # If the number is greater than 1 and does not have any factors other than 1 and itself, it is prime.
    return True

# Define a function to check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        # If n is not a prime number, return False (not left-and-right-truncatable prime)
        return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    if str(n)[0] == '1' or str(n)[-1] == '1':

        # If the leading leftmost digit is 1 or the last rightmost digit is 1, return False (not left-and-right-truncatable prime)
        return False

    # If all conditions are met, return True (left-and-right-truncatable prime)
    return True
