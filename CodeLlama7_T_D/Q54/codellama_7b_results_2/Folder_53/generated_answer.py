
def all_right_truncatable_prime(tuple):
    # Get the integer at index 86 from the tuple
    x = tuple[86]
    # Initialize an empty list to store the right-truncatable prime numbers less than x
    right_truncatable_primes = []
    # Iterate from 2 to x - 1
    for i in range(2, x):
        # Check if i is a prime number
        if is_prime(i):
            # Check if the last rightmost digit of i is successively removed, the result remains prime
            if is_prime(remove_last_rightmost_digit(i)) and is_prime(remove_last_but_one_rightmost_digit(i)) and is_prime(remove_all_but_last_rightmost_digits(i))):
                # If i is a right-truncatable prime number, add it to the list
                right_truncatable_primes.append(i)
    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(right_truncatable_primes, reverse=True)
# Define a function is_prime to check if a number is prime
def is_prime(n):
    # If n is not an integer or is less than 2, return False
    if not (isinstance(n, int) and n >= 2)):
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If no such number exists, return True
    return True

# Define a function remove_last_rightmost_digit to remove the last rightmost digit of an integer
def remove_last_rightmost_digit(n):
    # Get the string representation of n
    str_n = str(n)
    # Remove the last character from the string representation of n
    return int(str_n[:-1])

# Define a function remove_last_but_one_rightmost_digit to remove the last but one rightmost digit of an integer
def remove_last_but_one_rightmost_digit(n):
    # Get the string representation of n
    str_n = str(n)
    # Remove the last but one character from the string representation of n
    return int(str_n[:-2] + str_n[-1])

# Define a function remove_all_but_last_rightmost_digits to remove all but the last rightmost digit of an integer
def remove_all_but_last_rightmost_digits(n):
    # Get the string representation of n
    str_n = str(n)
    # Remove all but the last character from the string representation of n
    return int(str_n[-1])
