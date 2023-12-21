
def all_right_truncatable_prime(num):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the numbers from 1 to num - 1
    for i in range(1, num):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is right-truncatable prime
            if is_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of right-truncatable prime numbers less than num
    return prime_numbers

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to n - 1
        for i in range(2, n):
            # If the number is divisible by any other number except 1 and itself, it is not a prime number
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any other number except 1 and itself, it is a prime number
    return True

# Define a function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Initialize an empty string to store the last rightmost digit of the number
    last_digit = ""

    # Loop through the numbers from n - 1 to 1
    for i in range(n, 0, -1):
        # If the number is not a prime number, it is not a right-truncatable prime number
        if not is_prime(i):
            return False

        # Get the last rightmost digit of the number
        last_digit = str(i)[-1]

        # If the last rightmost digit of the number is not equal to 1, it is not a right-truncatable prime number
        if int(last_digit) != 1:
            return False

    # If the number is a prime number and it has only one rightmost digit that is equal to 1, it is a right-truncatable prime number
    return True
