
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        # Return False if n is not a prime number
        return False

    # Initialize an empty string to store the representation of n
    num_str = ""

    # Convert n to a string and store it in num_str
    num_str = str(n)

    # Check if the leading leftmost digit of n is 0
    if num_str[0] == "0":

        # Return False if the leading leftmost digit of n is 0
        return False

    # Initialize an empty string to store the representation of n without the leading leftmost digit
    new_num_str = ""

    # Remove the leading leftmost digit from num_str and store it in new_num_str
    new_num_str = num_str[1:]

    # Check if the last rightmost digit of n is 0
    if new_num_str[-1] == "0":

        # Return False if the last rightmost digit of n is 0
        return False

    # Initialize an empty string to store the representation of n without the last rightmost digit
    final_new_num_str = ""

    # Remove the last rightmost digit from new_num_str and store it in final_new_num_str
    final_new_num_str = new_num_str[:-1]

    # Check if n is equal to the product of its digits
    if int(final_new_num_str) == n:

        # Return True if n is a left-and-right-truncatable prime number
        return True
