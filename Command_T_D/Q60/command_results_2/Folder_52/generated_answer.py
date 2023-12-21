
import bisect

def all_left_right_truncatable_prime(x_range):
    primes = []
    for x in range(2, x_range[0] + 1):
        is_prime = True
        for i in range(2, int(str(x)[-1]) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    for x in range(x_range[1] + 1, int(str(x_range[1])[1:]) + 1):
        is_prime = True
        for i in range(2, int(str(x)[-1]) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    if len(primes) == 0:
        return []
    return sorted(primes, reverse=True)
