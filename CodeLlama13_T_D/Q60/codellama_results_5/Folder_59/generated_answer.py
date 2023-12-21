
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not str(i).startswith('0'):
            primes.append(i)
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            if (primes[j] % primes[i]) == 0:
                break
        else:
            primes[i] = primes[i-1] * primes[i]
    return sorted(set(primes), reverse=True)
