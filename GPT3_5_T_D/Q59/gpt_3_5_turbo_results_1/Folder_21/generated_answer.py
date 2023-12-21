
def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return primes

def all_left_truncatable_prime(nums):
    x = nums[175]
    primes = sieve(x)
    result = []
    for num in range(11, x):
        if str(num).count('0') == 0:
            trunc_primes = True
            for i in range(1, len(str(num))):
                if not primes[int(str(num)[i:])]:
                    trunc_primes = False
                    break
            if trunc_primes:
                result.append(num)
    return result
