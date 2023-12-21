
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x, and check if each number is a prime number
    for i in range(1, x + 1):

        # If the number is not a prime number, continue to the next iteration
        if not is_prime(i):
            continue


        # Check if the number is a left-and-right-truncatable prime number
        if is_left_right_truncatable_prime(i):

            # Add the number to the list of prime numbers
            prime_numbers.append(i)


    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):

    # If the number is less than 2, it is not prime
    if n < 2:
        return False


    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):

        # If the number is divisible by any number between 2 and the square root of the number, it is not prime
        if n % i == 0:
            return False


    # If the number is greater than 1 and it is divisible only by 1 and itself, it is prime
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # If the number is not a prime number, it cannot be a left-and-right-truncatable prime number
    if not is_prime(n):
        return False


    # Check if the number contains the digit 0
    if '0' in str(n):

        # If the number contains the digit 0, it cannot be a left-and-right-truncatable prime number
        return False


    # Check if the number is a left-truncatable prime number by removing all digits except for the last one
    last_digit = str(n)[-1]
    temp_number = int(str(n)[:-1])
    while temp_number > 0:

        # If the remaining number is not a prime number, it cannot be a left-and-right-truncatable prime number
        if not is_prime(temp_number):
            return False

        # Remove the last digit of the remaining number
        temp_digit = str(temp_number)[-1]
        temp_number = int(str(temp_number)[:-1]))

        # Check if the remaining number is a prime number
        if is_prime(temp_number):

            # If the remaining number is a prime number, it cannot be a left-and-right-truncatable prime number
            return False


    # Check if the number is a right-truncatable prime number by removing all digits except for the first one
    first_digit = str(n)[0]
    temp_number = int(str(n)[1:]))
    while temp_number > 0:

        # If the remaining number is not a prime number, it cannot be a left-and-right-truncatable prime number
        if not is_prime(temp_number):
            return False

        # Remove the first digit of the remaining number
        temp_digit = str(temp_number)[0]
        temp_number = int(str(temp_number)[1:]))

        # Check if the remaining number is a prime number
        if is_prime(temp_number):

            # If the remaining number is a prime number, it cannot be a left-and-right-truncatable prime number
            return False

    # If the number is a prime number and it is a left-and-right-truncatable prime number, it can be considered as one
    return True

# Check if a number is a prime number by using the Sieve of Eratosthenes algorithm
def is_prime(n):

    # If the number is less than 2 or is not an integer, it cannot be a prime number
    if n < 2 or (isinstance(n, int) and n % 1 != 0)):
        return False


    # Check if the number is a perfect square by using the Babylonian method to calculate its square root
    square_root = math.sqrt(n)
    if not math.isclose(square_root, int(square_root), rel_tol=1e-09)):
        return False


    # Check if the number is a left-truncatable prime number by removing all digits except for the last one
    last_digit = str(n)[-1]
    temp_number = int(str(n)[:-1]))
    while temp_number > 0:

        # If the remaining number is not a prime number, it cannot be a left-truncatable prime number
        if not is_prime(temp_number):
            return False

        # Remove the last digit of the remaining number
        temp_digit = str(temp_number)[-1]
        temp_number = int(str(temp_number)[:-1]))

        # Check if the remaining number is a prime number
        if is_prime(temp_number):

            # If the remaining number is a prime number, it cannot be a left-truncatable prime number
            return False

    # Check if the number is a right-truncatable prime number by removing all digits except for the first one
    first_digit = str(n)[0]
    temp_number = int(str(n)[1:]))
    while temp_number > 0:

        # If the remaining number is not a prime number, it cannot be a right-truncatable prime number
        if not is_prime(temp_number):
            return False

        # Remove the first digit of the remaining number
        temp_digit = str(temp_number)[0]
        temp_number = int(str(temp_number)[1:]))

        # Check if the remaining number is a prime number
        if is_prime(temp_number):

            # If the remaining number is a prime number, it cannot be a right-truncatable prime number
            return False

    # If the number is a prime number and it is a left-and-right-truncatable prime number, it can be considered as one
    return True
