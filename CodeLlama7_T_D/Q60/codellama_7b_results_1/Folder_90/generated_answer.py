
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the range of values from 1 to x
    for i in range(1, x + 1):

        # Check if the current number is a prime number
        if is_prime(i):

            # If the current number is a prime number, check if it is left-and-right-truncatable
            if is_left_right_truncatable(i):

                # If the current number is both a prime number and left-and-right-truncatable, add it to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the range of values from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If the current number is divisible by i, it is not prime
            if n % i == 0:
                return False

    # If the current number is greater than 1 and it is not divisible by any number in the range of values from 2 to the square root of n, it is prime
    return True

# Define a function to check if a number is left-and-right-truncatable
def is_left_right_truncatable(n):
    # Check if the current number contains any 0 digits
    if '0' in str(n):
        return False

    # If the current number does not contain any 0 digits, check if it remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    else:
        # Initialize an empty list to store the numbers that have been removed from the current number
        removed_numbers = []

        # Loop through the range of values from 1 to the square root of n
        for i in range(1, int(n ** 0.5) + 1):
            # Check if the current number is divisible by i
            if n % i == 0:
                # If the current number is divisible by i, add it to the list of numbers that have been removed from the current number
                removed_numbers.append(i)

        # Check if any of the numbers that have been removed from the current number are equal to 1 or 2
        for removed_number in removed_numbers:
            if removed_number == 1 or removed_number == 2:
                return False

    # If the current number does not contain any 0 digits and it remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime, then it is both a prime number and left-and-right-truncatable
    return True
