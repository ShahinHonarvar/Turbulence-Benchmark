
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in lst[2:3]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)
