
def all_left_right_truncatable_prime(tup):
    x = tup[74]
    primes = []
    for num in range(2, x + 1):
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
    res = []
    for prime in primes:
        if '0' not in str(prime):
            is_truncatable = True
            for i in range(1, len(str(prime))):
                if int(str(prime)[i:]) not in primes or int(str(prime)[:i]) not in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                res.append(prime)
    return sorted(res)
