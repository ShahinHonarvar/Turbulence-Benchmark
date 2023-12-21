
def find_primes_between_indices(list_integers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [x for x in list_integers[17:80] if is_prime(x)]
    prime_numbers.sort(reverse=True)
    return prime_numbers
