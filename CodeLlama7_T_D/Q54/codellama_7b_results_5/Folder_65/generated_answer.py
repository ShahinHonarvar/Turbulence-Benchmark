 def all_right_truncatable_prime(tuple):
    x = tuple[32]
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 10 to x
    for i in range(10, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is right-truncatable prime number
            if is_right_truncatable_prime(i):

                # Add the number to the list of prime numbers
                prime_list.append(i)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_list)

# Check if a number is a prime number
def is_prime(n):

    # Return True if n is a prime number
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    # If n <= 1, it is not a prime number
    else:
        return False

# Check if a number is right-truncatable prime number
def is_right_truncatable_prime(n):

    # Initialize a variable to store the last digit of the number
    last_digit = n % 10

    # Iterate from the second last digit to the first digit
    for i in range(len(str(n))) - 2, len(str(n)) - 1):

        # Check if the current digit is equal to the last digit
        if str(n)[i] == str(last_digit):

            # If it is equal, remove the current digit and check if the resulting number is a prime number
            n = int(str(n)[:i] + str(n)[i+1:]))

            # Check if the resulting number is a prime number
            if is_prime(n):

                # If it is a prime number, return True
                return True

    # If no such right-truncatable prime number exists, return False
    return False
