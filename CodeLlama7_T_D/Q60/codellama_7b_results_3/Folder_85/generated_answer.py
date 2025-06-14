
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than or equal to x
    for num in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(num):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):

                # Add the prime number to the list of prime numbers
                prime_numbers.append(num)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Check if n is divisible by 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                return False

        # If n is divisible by 2 to n-1 return True
        return True

def is_left_right_truncatable_prime(n):

    # Check if n contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the leading leftmost digit of n is not a 1
    if int(str(n)[0]) == 1:
        return False

    # Check if the last rightmost digit of n is not a 1
    if int(str(n)[-1]) == 1:
        return False

    # Check if n is still prime after removing the leading leftmost and last rightmost digits
    return is_prime(int(str(n))[1:-1]))
