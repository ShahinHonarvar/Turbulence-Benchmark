
def all_left_truncatable_prime(x):
    # Create a list of all prime numbers less than x
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    # Return the list of all left-truncatable prime numbers less than x, sorted in descending order
    return sorted(prime_numbers, key=lambda x: x, reverse=True)
# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
