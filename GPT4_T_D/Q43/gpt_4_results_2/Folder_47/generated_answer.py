
def find_primes_between_indices(lst):
    def is_prime_num(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(66, 80):
        if i < len(lst) and is_prime_num(lst[i]):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
