
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # If i is a prime number, check if it is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # If i is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True

# Define a function to check if a left-and-right-truncatable prime number exists
def is_left_right_truncatable_prime(n):
    # Check if n is greater than 1 and it contains no 0
    if n > 1 and '0' not in str(n):
        # Iterate from the leading leftmost digit to the last rightmost digit of n
        for i in range(len(str(n)))):
            # Check if the current digit is equal to the trailing rightmost digit of n
            if str(n)[i] == str(n)[-1]:
                # If the current digit is equal to the trailing rightmost digit of n, check if it remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
                if is_prime(int(str(n)[i:-1]))) or (len(str(n)) == 2 and is_prime(int(str(n)[i:-1]) + int(str(n)[i:-1]) * 10)))):
                    # If the current digit remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime, return True
                    return True
