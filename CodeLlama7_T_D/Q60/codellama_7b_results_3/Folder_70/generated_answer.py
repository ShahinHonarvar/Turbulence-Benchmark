
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate through the range of numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_list.append(i)

    # Sort the list in descending order
    prime_list.sort(reverse=True)

    # Return the list of prime numbers
    return prime_list

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not prime
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, then it is prime
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, then it is not a left-and-right-truncatable prime number
        return False

    # Check if the leading leftmost digit of n is equal to 1
    if int(str(n)[0]) != 1:
        # If the leading leftmost digit of n is not equal to 1, then it is not a left-and-right-truncatable prime number
        return False

    # Check if the last rightmost digit of n is equal to 1
    if int(str(n)[-1])) != 1:
        # If the last rightmost digit of n is not equal to 1, then it is not a left-and-right-truncatable prime number
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)))):
        # Check if the number after removing the leading leftmost digit is equal to 1
        if int(str(n)[i + 1])) != 1:
            # If the number after removing the leading leftmost digit is not equal to 1, then it is not a left-and-right-truncatable prime number
            return False

    # If all the checks are successful, then n is a left-and-right-truncatable prime number
    return True
