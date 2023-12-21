
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number using the Sieve of Eratosthenes
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number by removing the leading leftmost and last rightmost digits
            if is_left_right_truncatable_prime(i):

                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Function to check if a number is prime using the Sieve of Eratosthenes
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it is not divisible by 2 to n-1, then it is prime
    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number contains any 0
    if '0' in str(n):
        return False

    # Check if the number is a palindrome
    if str(n) == str(n)[::-1]:

        # Remove the leading leftmost and last rightmost digits of the number to check if it remains prime after truncation
        leading_leftmost = int(str(n)[:2])
        last_rightmost = int(str(n)[-2:]))

        # Check if the number is still a prime after removing the leading leftmost and last rightmost digits
        if is_prime(leading_leftmost) and is_prime(last_rightmost):
            return True

    # If the number does not contain any 0 and it is not a palindrome, then it is not a left-and-right-truncatable prime number
    return False
