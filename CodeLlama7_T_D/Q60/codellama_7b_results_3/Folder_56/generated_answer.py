
def all_left_right_truncatable_prime(num_tuple):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate through each number in the tuple
    for num in num_tuple:

        # Check if the number is a prime number
        if is_prime(num):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):

                # Add the prime number to the list
                prime_list.append(num)

    # Return the sorted list of prime numbers
    return sorted(prime_list)

# Define a function to check if a number is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Check if n is divisible by 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                return False

        # If n is divisible by any number between 2 and n-1, it is not prime
        return True

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is less than 3
    if n < 3:
        return False

    # Check if n contains any zero digits
    if '0' in str(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, len(str(n)))):
        num = int(str(n)[i:] + str(n)[:i])
        if is_prime(num):
            return True

    # If the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime, then it is not left-and-right-truncatable prime number
    return False
