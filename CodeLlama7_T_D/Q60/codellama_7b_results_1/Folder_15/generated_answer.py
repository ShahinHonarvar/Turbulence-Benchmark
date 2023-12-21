
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_list.append(i)

    # Sort the list in descending order
    prime_list.sort(reverse=True)

    # Return the list of prime numbers
    return prime_list

# Define a function to check if a number is a prime number
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the loop completes successfully, return True
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n contains no 0
    if "0" in str(n):
        return False

    # Iterate from 1 to the length of the number - 1
    for i in range(1, len(str(n)))):

        # Remove the leading leftmost and last rightmost digits of n simultaneously successively removed down to a one- or two-digit prime.
        temp = str(n)[:i] + str(n)[i+1:]

        # Check if the resulting number is a prime number
        if is_prime(int(temp))):
            return True

    # If the loop completes successfully, return False
    return False
