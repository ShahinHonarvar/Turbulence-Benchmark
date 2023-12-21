
def find_primes_between_indices(my_list):
    # Find all prime numbers in the specified range
    prime_numbers = []
    for i in range(67, 88):
        if is_prime(i):
            prime_numbers.append(i)
    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers

def is_prime(n):
    # Check if 'n' is a prime number
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
