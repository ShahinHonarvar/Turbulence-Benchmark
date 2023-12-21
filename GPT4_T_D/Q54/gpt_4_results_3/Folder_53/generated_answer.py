
def all_right_truncatable_prime(t):
    x = t[86]
    prime_list = absolute_prime(x)
    right_truncatable_primes = [i for i in prime_list if right_truncated_prime(i)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def absolute_prime(n):
    primes = []
    sieve = [True] * n
    for x in range(2, n):
        if sieve[x]:
            primes.append(x)
            for i in range(x, n, x):
                sieve[i] = False
    return primes

def right_truncated_prime(n):
    str_n = str(n)
    for ind in range(len(str_n)):
        if not absolute_prime(int(str_n[0:len(str_n) - ind])):
            return False
    return True
