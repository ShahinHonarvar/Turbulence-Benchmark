
def all_left_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and '0' not in str(i):
            primes.append(i)
    return sorted([int(''.join(map(str, primes[:j]))) for j in range(len(primes))])
