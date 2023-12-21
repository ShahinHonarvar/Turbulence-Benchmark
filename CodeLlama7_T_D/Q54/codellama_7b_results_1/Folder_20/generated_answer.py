 def all_right_truncatable_prime(tuple):
    x = tuple[100]
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    for i in range(2, x + 1):
        # Check if the number is a prime number
        if is_prime(i) == True:
            # Check if the number is right-truncatable prime number
            if is_right_truncatable_prime(i) == True:
                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)
    # Sort the list in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):

    # Check if the number is a prime number
    if is_prime(n) == False:
        return False

    # Check if the number is right-truncatable prime number
    for i in range(1, len(str(n)))):
        # If the last rightmost digit of the number is not a prime number, then it is not a right-truncatable prime number.
        if is_prime(int(str(n)[:-i]))) == False:
            return False

    return True
