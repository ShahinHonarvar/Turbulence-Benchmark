
def all_right_truncatable_prime(num_tuple):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n_str = str(n)
        while len(n_str) > 0:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True

    x = num_tuple[97]
    primes = []

    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)

    return sorted(primes)
