
def find_primes_between_indices(lst):
    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in lst[415:648] if check_prime(x)]
    return sorted(primes)
