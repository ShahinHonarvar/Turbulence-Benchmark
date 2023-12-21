
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left- and right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Initialize an empty string to store the number in string format
    num_str = ''

    # Convert the number to string format
    while n > 0:
        num_str += str(n % 10)
        n //= 10

    # Check if the number is a left-truncatable prime number
    for i in range(len(num_str)):
        if not is_prime(int(num_str[:i] + num_str[i+1:])))
            return False

    # Check if the number is a right-truncatable prime number
    for i in range(len(num_str)-1, -1, -1):
        if not is_prime(int(num_str[:i] + num_str[i+1:])))
            return False

    # Return True if the number is a left-and-right-truncatable prime number
    return True
