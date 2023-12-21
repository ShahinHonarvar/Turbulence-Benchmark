
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in lst[31:93] if is_prime(i)]
    primes.sort(reverse=True)
    return primes
