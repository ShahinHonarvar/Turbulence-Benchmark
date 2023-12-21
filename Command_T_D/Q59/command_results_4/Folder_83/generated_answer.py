import math
def all_left_truncatable_prime(n):
    l = []
    for i in range(3, int(math.ceil(math.sqrt(n[24])) + 1):
        a = str(i)
        j = len(a) - 1
        while j >= 1 and a[j] == '0':
            a = a[:j]
            j -= 1
        if a:
            if all(int(a[i]) for i in range(1, len(a))):
                if all(isPrime(int(a[i])) for i in range(1, len(a))):
                    l.append(int(a))
    return l
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = n**0.5
    i = 5
    while i * i <= maxDivisor:
        if n % i == 0:
            return False
        i += 6
    return True
