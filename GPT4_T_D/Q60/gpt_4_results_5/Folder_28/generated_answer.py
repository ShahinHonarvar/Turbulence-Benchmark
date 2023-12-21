
def all_left_right_truncatable_prime(t):
    x = t[19]
    primes = [True] * (x + 1)
    res = []

    for i in range(2, x + 1):
        if primes[i]:
            for j in range(i << 1, x + 1, i):
                primes[j] = False
            if i > 10:
                if '0' in str(i):
                    continue
                left = i // 10
                right = i % (10 ** (len(str(i)) - 1))
                while left > 10 and right > 10:
                    if not primes[left] or not primes[right]:
                        break
                    left //= 10
                    right %= (10 ** (len(str(right)) - 1))
                else:
                    if primes[left] and primes[right]:
                        res.append(i)
    return sorted(res)
