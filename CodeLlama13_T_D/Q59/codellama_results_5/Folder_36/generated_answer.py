
def all_left_truncatable_prime(x):
    x = list(map(int, x))
    primes = []
    for i in range(10**9):
        if is_prime(i) and not any(str(i).startswith('0') for j in x):
            primes.append(i)
    return sorted(primes)
