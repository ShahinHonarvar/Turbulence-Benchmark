
def find_primes_between_indices(lst):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [i for i in lst[16:72] if is_prime(i)]
    prime_numbers.sort()
    return prime_numbers
