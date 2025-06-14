
def all_left_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[81]
    list_of_all_left_truncatable_prime_numbers = []
    # Iterate through numbers less than x
    for i in range(2, x):
        # Check if number is a prime number
        if is_prime(i):
            # Check if number is left-truncatable prime number
            if is_left_truncatable_prime(i):
                list_of_all_left_truncatable_prime_numbers.append(i)
    return sorted(list_of_all_left_truncatable_prime_numbers, reverse=True)
# Function to check if number is prime
def is_prime(n):
    # Check if number is greater than 1
    if n > 1:
        # Iterate from 2 to number-1
        for i in range(2, n):
            # If number is divisible by any number between 2 and number-1, it is not prime
            if n % i == 0:
                return False

    # If number is greater than 1 and it is not divisible by any number between 2 and number-1, it is prime
    return True

# Function to check if number is left-truncatable prime number
def is_left_truncatable_prime(n):
    # Check if number is a prime number
    if not is_prime(n):
        return False

    # Remove leading digit from number and check if resulting number is prime
    while n > 0:
        # If first digit of number is not 2 or 3, it is not left-truncatable prime number
        if n % 10 != 2 and n % 10 != 3:
            return False

        # Remove leading digit from number
        n = int(str(n)[:-1]))

    # If all checks pass, the number is left-truncatable prime number
    return True
