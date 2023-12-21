
def all_left_truncatable_prime(tuple):
    x = tuple[88]
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    for i in range(2, x):
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        # If the number is a prime number and it is left-truncatable prime, then add it to the list of prime numbers
        if is_prime and is_left_truncatable_prime(i):
            prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers

# Function to check if a number is left-truncatable prime or not
def is_left_truncatable_prime(n):
    # If the number does not contain any 0, then it is left-truncatable prime
    if '0' not in str(n):
        return True

    # Otherwise, check if all the leading leftmost digits are successively removed, then all resulting numbers are prime
    else:
        for i in range(1, len(str(n)))):
            num = int(str(n)[:-i])
            if not is_prime(num):
                return False

        # If all the leading leftmost digits are successively removed and all resulting numbers are prime, then the number is left-truncatable prime
        return True

# Function to check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            return False

    return True
