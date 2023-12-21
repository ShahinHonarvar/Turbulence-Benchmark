
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all prime numbers less than or equal to x
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            # If the current number is a left-and-right-truncatable prime number, add it to the list of prime numbers
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number using the Sieve of Eratosthenes algorithm
def is_prime(n):
    # If n is less than 2, it is not a prime number
    if n < 2:
        return False

    # Loop through all numbers from 2 to sqrt(n)
    for i in range(2, int(sqrt(n)) + 1)):
        # If the current number is divisible by any other number between 2 and sqrt(n), it is not a prime number
        if n % i == 0:
            return False

    # If the current number is greater than 1 and it has not been divisible by any other number between 2 and sqrt(n), it is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number using the definition of such a number given in the problem statement
def is_left_right_truncatable_prime(n):
    # If n is less than 2, it is not a left-and-right-truncatable prime number
    if n < 2:
        return False

    # Convert the current number to a string and extract the leading leftmost and last rightmost digits
    s = str(n)
    leading_leftmost = s[0]
    last_rightmost = s[-1]

    # Check if the leading leftmost digit is not equal to 0, and if the last rightmost digit is not equal to 0
    if leading_leftmost == '0' or last_rightmost == '0':
        return False

    # Convert the current number back to an integer and check if it remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    n = int(s)
    while len(str(n)) > 1:
        if not is_prime(n):
            return False

        # Remove the leading leftmost digit of the current number by dividing it by 10 and taking the remainder as the new leading leftmost digit
        n = int(s) // 10 + (int(s) % 10))

    # If the current number remains prime when all digits are simultaneously successively removed down to a one- or two-digit prime, it is a left-and-right-truncatable prime number
    return True
