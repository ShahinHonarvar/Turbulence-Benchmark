
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_list.append(i)

    # Sort the prime list in descending order
    prime_list.sort(reverse=True)

    # Return the prime list
    return prime_list

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # Check if i divides n
            if n % i == 0:
                # Return False if there exists a divisor of n other than 1 and itself
                return False

    # Return True if n is a prime number, else return False
    return n > 1

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize an empty string to store the number in string format
    num_str = ""

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Append the current digit of the number to the string
        num_str += str(i)

        # Check if the string is a valid prime number
        if is_prime(int(num_str)):
            # Return True if the string is a valid left-and-right-truncatable prime number, else return False
            return True

    # Return False if no left-and-right-truncatable prime number exists in the specified range
    return False
