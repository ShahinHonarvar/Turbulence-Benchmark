
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the elements of the tuple
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # If it is a prime number, append it to the list of prime numbers
            prime_numbers.append(element)

    # Loop through the elements of the list of prime numbers
    for element in prime_numbers:
        # Check if the element is a right-truncatable prime number
        if is_right_truncatable_prime(element):
            # If it is a right-truncatable prime number, append it to the list of right-truncatable prime numbers
            right_truncatable_prime_numbers.append(element)

    # Sort the list of right-truncatable prime numbers in descending order
    sorted_right_truncatable_prime_numbers = sorted(right_truncatable_prime_numbers, reverse=True)

    # Return the sorted list of right-truncatable prime numbers less than x
    return sorted_right_truncatable_prime_numbers

# Define a function to check if a number is a prime number
def is_prime(number):
    # Check if the number is greater than 1
    if number > 1:
        # Loop through the numbers from 2 to the square root of the number
        for i in range(2, int(number ** 0.5) + 1)):
            # Check if any of the numbers divides the number without a remainder
            if number % i == 0:
                # If it does, the number is not prime
                return False

        # If none of the numbers divide the number without a remainder, the number is prime
        return True

    # If the number is less than or equal to 1, it is not prime
    else:
        return False

# Define a function to check if a right-truncatable prime number is still prime after the last rightmost digit has been removed
def is_right_truncatable_prime(number):
    # Check if the number is greater than 1
    if number > 1:
        # Loop through the numbers from 2 to the square root of the number
        for i in range(2, int(number ** 0.5) + 1)):
            # Check if any of the numbers divides the number without a remainder
            if number % i == 0:
                # If it does, the number is not prime
                return False

        # If none of the numbers divide the number without a remainder, the number is prime
        return True

    # If the number is less than or equal to 1, it is not prime
    else:
        return False

# Define a function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(number):
    # Check if the number is greater than 1
    if number > 1:
        # Loop through the numbers from 2 to the square root of the number
        for i in range(2, int(number ** 0.5) + 1)):
            # Check if any of the numbers divides the number without a remainder
            if number % i == 0:
                # If it does, the number is not prime
                return False

        # If none of the numbers divide the number without a remainder, the number is prime
        return True

    # If the number is less than or equal to 1, it is not prime
    else:
        return False
