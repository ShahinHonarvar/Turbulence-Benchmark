
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all the prime numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_list.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_list, reverse=True)

# Check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all the integers between 2 and n - 1
        for i in range(2, n):

            # If the remainder of n divided by i is zero, return False
            if n % i == 0:
                return False

    # Return True if n is greater than 1 and has no divisors other than 1 and itself
    return n > 1

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Initialize an empty string to store the digits of n
    digits = ""

    # Loop through all the digits of n
    for digit in str(n):

        # Add each digit to the string of digits
        digits += digit

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    return all(is_prime(int(digits[:i] + digits[i+1:])) for i in range(len(digits))))
