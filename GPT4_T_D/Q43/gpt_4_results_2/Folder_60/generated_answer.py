
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if 46 <= len(lst)-1 and 85 <= len(lst)-1:
        primes = [i for i in lst[46:86] if is_prime(i)]
    else:
        primes = []
    return sorted(primes)
