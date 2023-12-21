
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the list of prime numbers sorted in descending order
    return sorted(prime_numbers, reverse=True)

# Define a function to check if an integer is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n (inclusive)
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

# Define a function to check if an integer is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n (inclusive)
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Check if n contains the digit 0
    if str(n).find('0') != -1:
        # Return False if n contains the digit 0
        return False

    # Initialize an empty list to store the left and right truncatable prime numbers
    left_right_truncatable_prime_numbers = []

    # Iterate from 2 to the square root of n (inclusive)
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if removing the leading leftmost and last rightmost digits from i results in a one- or two-digit prime number
            if str(i)[1:] == '':
                # Add i to the list of left-and-right-truncatable prime numbers
                left_right_truncatable_prime_numbers.append(i)
            elif len(str(i)) == 2 and str(i)[0] == '1' or str(i)[0] == '2':
                # Add i to the list of left-and-right-truncatable prime numbers
                left_right_truncatable_prime_numbers.append(i)

    # Return True if n is a left-and-right-truncatable prime number and False otherwise
    return len(left_right_truncatable_prime_numbers) > 0
