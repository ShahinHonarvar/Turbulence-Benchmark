
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x (both inclusive)
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_list.append(i)

    # Sort the list of prime numbers in descending order
    prime_list.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_list

# Check if a number is a prime number
def is_prime(n):
    # If n is less than 2, it is not a prime number
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If n is divisible only by 1 and itself, it is a prime number
    return True

# Check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):
    # If n is less than 3, it is not a left-and-right-truncatable prime number
    if n < 3:
        return False

    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Remove the leading leftmost and last rightmost digits from n
    leading_leftmost = int(str(n)[1:] * 0.1)
    trailing_rightmost = int(str(n)[:-1])

    # Check if the number of digits in the removed leftmost and rightmost digits is less than or equal to 2
    if len(str(leading_leftmost)) > 2 or len(str(trailing_rightmost)) > 2:
        return False

    # Check if n is still a prime number after removing the leading leftmost and last rightmost digits
    if not is_prime(n - leading_leftmost - trailing_rightmost):
        return False

    # If all checks pass, n is a left-and-right-truncatable prime number
    return True
