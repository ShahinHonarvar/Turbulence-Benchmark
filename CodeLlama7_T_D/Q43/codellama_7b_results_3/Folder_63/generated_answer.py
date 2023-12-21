
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(28, 36 + 1):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True
